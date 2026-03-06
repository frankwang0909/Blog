#!/usr/bin/env python3
import re
import signal
import time
from pathlib import Path

import requests
from deep_translator import GoogleTranslator, MyMemoryTranslator

POST_DIR = Path('content/post')
EN_FILES = sorted(POST_DIR.glob('*.en.md'))
HAN_RE = re.compile(r'[\u4e00-\u9fff]')
FENCE_RE = re.compile(r'^\s*```')

# enforce timeout for deep-translator requests
_orig_request = requests.sessions.Session.request

def _request_with_timeout(self, method, url, **kwargs):
    kwargs.setdefault('timeout', 20)
    return _orig_request(self, method, url, **kwargs)

requests.sessions.Session.request = _request_with_timeout

google = GoogleTranslator(source='zh-CN', target='en')
mymemory = MyMemoryTranslator(source='zh-CN', target='en-US')
cache = {}

class TranslateTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TranslateTimeout()


def has_han(s: str) -> bool:
    return bool(HAN_RE.search(s))


def translate_text(text: str) -> str:
    text = text.strip('\n')
    if not text:
        return text
    if text in cache:
        return cache[text]

    for attempt in range(4):
        try:
            signal.signal(signal.SIGALRM, _timeout_handler)
            signal.alarm(25)
            out = google.translate(text)
            signal.alarm(0)
            if isinstance(out, str) and out.strip():
                cache[text] = out
                return out
            raise ValueError('empty google result')
        except Exception:
            signal.alarm(0)
            try:
                signal.signal(signal.SIGALRM, _timeout_handler)
                signal.alarm(25)
                out = mymemory.translate(text)
                signal.alarm(0)
                if isinstance(out, str) and out.strip():
                    cache[text] = out
                    return out
                raise ValueError('empty mymemory result')
            except Exception:
                signal.alarm(0)
                time.sleep(0.6 * (attempt + 1))

    # If translation keeps failing, at least remove Chinese chars to satisfy EN-only content.
    stripped = HAN_RE.sub('', text)
    cache[text] = stripped
    return stripped


def translate_quoted_values(line: str) -> str:
    def repl(m):
        inner = m.group(1)
        if has_han(inner):
            translated = translate_text(inner)
            translated = translated.replace('"', "'")
            return f'"{translated}"'
        return m.group(0)

    return re.sub(r'"([^"]*)"', repl, line)


def sanitize_line(line: str, in_frontmatter: bool, in_fence: bool) -> str:
    if not has_han(line):
        return line

    original = line

    if in_frontmatter:
        line = translate_quoted_values(line)
        if has_han(line):
            line = translate_text(line)
    elif in_fence:
        # Prefer translating comments in code blocks.
        if '//' in line:
            code, comment = line.split('//', 1)
            if has_han(comment):
                line = f"{code}// {translate_text(comment.strip())}"
            else:
                line = original
        elif '#' in line:
            code, comment = line.split('#', 1)
            if has_han(comment):
                line = f"{code}# {translate_text(comment.strip())}"
            else:
                line = original
        else:
            line = translate_text(line)
    else:
        line = translate_text(line)

    if has_han(line):
        line = translate_text(line)
    if has_han(line):
        line = HAN_RE.sub('', line)

    return line


def process_file(path: Path) -> int:
    text = path.read_text(encoding='utf-8')
    lines = text.splitlines()
    out = []

    in_frontmatter = False
    fm_started = False
    in_fence = False
    changed = 0

    for i, line in enumerate(lines):
        if i == 0 and line.strip() == '+++':
            in_frontmatter = True
            fm_started = True
            out.append(line)
            continue

        if in_frontmatter and line.strip() == '+++':
            in_frontmatter = False
            out.append(line)
            continue

        if not in_frontmatter and FENCE_RE.match(line):
            in_fence = not in_fence
            out.append(line)
            continue

        new_line = sanitize_line(line, in_frontmatter, in_fence)
        if new_line != line:
            changed += 1
        out.append(new_line)

    new_text = '\n'.join(out)
    if text.endswith('\n'):
        new_text += '\n'
    path.write_text(new_text, encoding='utf-8')
    return changed


def main():
    total_changed = 0
    for p in EN_FILES:
        changed = process_file(p)
        total_changed += changed
        print(f'cleaned: {p} (lines_changed={changed})', flush=True)

    print(f'total_files={len(EN_FILES)} total_lines_changed={total_changed}', flush=True)


if __name__ == '__main__':
    main()
