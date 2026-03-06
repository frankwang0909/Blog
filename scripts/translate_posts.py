#!/usr/bin/env python3
import argparse
import re
import signal
import time
from pathlib import Path
import requests
from deep_translator import GoogleTranslator, MyMemoryTranslator

POST_DIR = Path('content/post')

google_translator = GoogleTranslator(source='zh-CN', target='en')
mymemory_translator = MyMemoryTranslator(source='zh-CN', target='en-US')

# deep-translator does not pass timeout, so enforce a sane network timeout globally.
_orig_request = requests.sessions.Session.request


def _request_with_timeout(self, method, url, **kwargs):
    kwargs.setdefault("timeout", 20)
    return _orig_request(self, method, url, **kwargs)


requests.sessions.Session.request = _request_with_timeout

CODE_FENCE_RE = re.compile(r'^\s*```')


def split_front_matter(text: str):
    if text.startswith('+++\n'):
        end = text.find('\n+++\n', 4)
        if end != -1:
            return text[: end + 5], text[end + 5 :]
    return '', text


def chunk_text(s: str, max_len: int = 4200):
    if len(s) <= max_len:
        return [s]
    parts = []
    buf = []
    n = 0
    for para in s.split('\n\n'):
        add = len(para) + (2 if buf else 0)
        if n + add > max_len and buf:
            parts.append('\n\n'.join(buf))
            buf = [para]
            n = len(para)
        else:
            buf.append(para)
            n += add
    if buf:
        parts.append('\n\n'.join(buf))
    return parts


def should_translate(line: str) -> bool:
    t = line.strip()
    if not t:
        return False
    if t.startswith('>'):
        return True
    if re.match(r'^\s*(!\[[^\]]*\]\([^\)]*\)|\[[^\]]+\]\([^\)]*\))\s*$', t):
        return False
    if re.match(r'^\s*<[^>]+>\s*$', t):
        return False
    if re.match(r'^\s*[-*]{3,}\s*$', t):
        return False
    return True


class TranslateTimeout(Exception):
    pass


def _timeout_handler(signum, frame):
    raise TranslateTimeout()


def translate_once(text: str) -> str:
    signal.signal(signal.SIGALRM, _timeout_handler)
    signal.alarm(25)
    try:
        result = google_translator.translate(text)
        if not isinstance(result, str) or not result.strip():
            raise ValueError("empty google translation result")
        return result
    except Exception:
        signal.alarm(0)
        signal.alarm(25)
        try:
            result = mymemory_translator.translate(text)
            if not isinstance(result, str) or not result.strip():
                raise ValueError("empty mymemory translation result")
            return result
        finally:
            signal.alarm(0)
    finally:
        signal.alarm(0)


def translate_block(block: str) -> str:
    chunks = chunk_text(block)
    out = []
    for ch in chunks:
        for attempt in range(5):
            try:
                out.append(translate_once(ch))
                break
            except Exception:
                if attempt == 4:
                    out.append(ch)
                else:
                    time.sleep(1.2 * (attempt + 1))
    return '\n\n'.join(out)


def translate_markdown_body(body: str) -> str:
    lines = body.splitlines()
    out = []
    in_fence = False
    buffer = []

    def flush_buffer():
        nonlocal buffer
        if not buffer:
            return
        text = '\n'.join(buffer)
        out.extend(translate_block(text).split('\n'))
        buffer = []

    for line in lines:
        if CODE_FENCE_RE.match(line):
            flush_buffer()
            in_fence = not in_fence
            out.append(line)
            continue

        if in_fence:
            out.append(line)
            continue

        if should_translate(line):
            buffer.append(line)
        else:
            flush_buffer()
            out.append(line)

    flush_buffer()
    result = '\n'.join(out)
    if body.endswith('\n') and not result.endswith('\n'):
        result += '\n'
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0, help="limit files for testing")
    parser.add_argument("--start-from", default="", help="start processing from this basename (without .md)")
    args = parser.parse_args()

    zh_files = sorted(p for p in POST_DIR.glob('*.md') if not p.name.endswith('.en.md'))
    if args.start_from:
        start_name = args.start_from
        zh_files = [p for p in zh_files if p.stem >= start_name]
    if args.limit > 0:
        zh_files = zh_files[: args.limit]

    count = 0
    for zh_path in zh_files:
        en_path = zh_path.with_name(zh_path.stem + '.en.md')
        if not en_path.exists():
            continue

        zh_text = zh_path.read_text(encoding='utf-8')
        zh_fm, zh_body = split_front_matter(zh_text)
        if not zh_body.strip():
            continue

        en_text = en_path.read_text(encoding='utf-8')
        en_fm, _ = split_front_matter(en_text)
        if not en_fm:
            en_fm = zh_fm

        translated_body = translate_markdown_body(zh_body)
        en_path.write_text(en_fm + translated_body, encoding='utf-8')
        count += 1
        print(f'translated: {en_path}', flush=True)

    print(f'total_translated={count}', flush=True)


if __name__ == '__main__':
    main()
