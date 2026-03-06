#!/usr/bin/env python3
import re
from pathlib import Path

POST_DIR = Path('content/post')
FILES = sorted(POST_DIR.glob('*.en.md'))

REPLACEMENTS = [
    (r'\bAngular2\b', 'Angular 2'),
    (r'\binstruction\b', 'directive'),
    (r'\binstructions\b', 'directives'),
    (r'\bStructure instructions\b', 'Structural directives'),
    (r'\bCustom instructions\b', 'Custom directives'),
    (r'\bServe\b', 'service'),
    (r'\bwindow operating systems\b', 'Windows operating systems'),
    (r'\bClass Class\b', 'Classes'),
    (r'\binterface Interface\b', 'interfaces'),
    (r'\bComponents components\b', 'Components'),
    (r'\bDirectives directive\b', 'Directives'),
    (r'\bModules module\b', 'Modules'),
    (r'\bDependency Injection Dependency Injection\b', 'Dependency Injection'),
    (r'\bQuickly get started with\b', 'A quick introduction to'),
    (r'\brealize\b', 'implement'),
    (r'\bRealize\b', 'Implement'),
    (r'\bThe results are as follows\b', 'The output looks like this'),
    (r'\bIf you add a parameter available, list all downloadable node\.js versions:\b', 'With the `available` flag, you can list all downloadable Node.js versions:'),
    (r'\bonline real-time compilation\b', 'online playground'),
    (r'\bgrammatical feature\b', 'language feature'),
    (r'\bVisual Studio Code itself is a `text editor`, which is very lightweight\. With various plug-ins, it can reproduce the powerful functions of Visual Studio\.', 'Visual Studio Code is a lightweight editor, and with extensions it provides many of Visual Studio\'s advanced capabilities.'),
    (r'\bAs long as you want, you can always find a situation where English is used\.', 'If you are intentional, you can always create opportunities to use English.'),
    (r'\bAs long as the `let command` exists in the `block-level scope`, the variables declared by it are "binding" to this area and are no longer affected by external influences\.', 'Once a variable is declared with `let` inside a block scope, that binding only exists in that scope and is not affected by outer scopes.'),
    (r'\bThe variable cannot be used in the area before the let command declares the variable, even if the variable is declared externally\.', 'The variable cannot be accessed before the `let` declaration within that scope, even if a variable with the same name exists outside it.'),
    (r'\bTypeScript is the officially recommended development language for `Angular 2`\.', 'TypeScript is the officially recommended language for `Angular 2` development.'),
    (r'\b3\.2 Online compilation: TypeScript officially provides \[online playground\] \(http://www\.typescriptlang\.org/play/index\.html\)\.', '3.2 Online compilation: TypeScript provides an official [online playground](http://www.typescriptlang.org/play/index.html).'),
]

LINE_REWRITES = {
    '## 1.Components': '## 1. Components',
    '### 2.2 Structural directives:': '### 2.2 Structural directives',
    '### 2.3 Custom directives:': '### 2.3 Custom directives',
}


def polish(text: str) -> str:
    out = text
    for pattern, repl in REPLACEMENTS:
        out = re.sub(pattern, repl, out)

    lines = out.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if s in LINE_REWRITES:
            indent = line[: len(line) - len(line.lstrip())]
            lines[i] = indent + LINE_REWRITES[s]
        # normalize extra spaces after list numbers
        lines[i] = re.sub(r'^(\d+)\.(\S)', r'\1. \2', lines[i])
    out = '\n'.join(lines)
    if text.endswith('\n') and not out.endswith('\n'):
        out += '\n'
    return out


def main():
    total = 0
    for p in FILES:
        src = p.read_text(encoding='utf-8')
        dst = polish(src)
        if dst != src:
            p.write_text(dst, encoding='utf-8')
            total += 1
            print(f'polished: {p}')
    print(f'total_polished={total}')


if __name__ == '__main__':
    main()
