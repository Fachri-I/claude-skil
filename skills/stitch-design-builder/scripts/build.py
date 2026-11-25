#!/usr/bin/env python3
"""Assemble final files from sources that use placeholders.

Usage: python build.py <src_dir> <out_dir>

<src_dir>/blocks/{global,reminder,guard,ds,refine}.txt hold the shared blocks.
Every *.md file in <src_dir> is copied to <out_dir> (same name) after replacing
{{REFINE}} first (it contains {{GUARD}}), then {{GUARD}}, {{DS}}, {{GLOBAL}}, {{REMINDER}}.
Fails if any {{placeholder}} is left over.
"""
import pathlib, re, sys

def main(src, out):
    src, out = pathlib.Path(src), pathlib.Path(out)
    out.mkdir(parents=True, exist_ok=True)
    blocks = {}
    for name in ('global', 'reminder', 'guard', 'ds', 'refine'):
        f = src / 'blocks' / f'{name}.txt'
        if f.exists():
            blocks[name.upper()] = f.read_text().strip('\n')
    order = ['REFINE', 'GUARD', 'DS', 'GLOBAL', 'REMINDER']
    built = []
    for f in sorted(src.glob('*.md')):
        t = f.read_text().rstrip('\n')
        for k in order:
            if k in blocks:
                t = t.replace('{{' + k + '}}', blocks[k])
        left = re.findall(r'\{\{.*?\}\}', t)
        if left:
            sys.exit(f'ERROR {f.name}: unresolved placeholders {sorted(set(left))}')
        (out / f.name).write_text(t + '\n')
        built.append(f.name)
    print('built:', ', '.join(built))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
