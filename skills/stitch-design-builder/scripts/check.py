#!/usr/bin/env python3
"""Consistency checks for a Stitch package.

Usage: python check.py <out_dir> [--max-words 250] [--allow-checked]

Expects DESIGN.md, 00-*.md (consistency file with the Global Prompt) and 02-*.md (prompt files).
Checks: hex tokens (DESIGN.md <-> Global Prompt <-> prompt files), Global Prompt identical in every
file that carries it, no leftover placeholders, all checkboxes reset, prompt length.
Lines starting with '>' (notes) are ignored for hex checks. Exit code 1 on any error.
"""
import pathlib, re, sys

HEX = re.compile(r'#[0-9A-Fa-f]{6}\b')
MARK = 'permanent design system'

def hexes(text):
    lines = [l for l in text.splitlines() if not l.lstrip().startswith('>')]
    return {h.upper() for h in HEX.findall('\n'.join(lines))}

def code_blocks(text):
    return re.findall(r'```\n(.*?)\n```', text, flags=re.S)

def main():
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    out = pathlib.Path(args[0])
    max_words = int(args[args.index('--max-words') + 1]) if '--max-words' in args else 250
    allow_checked = '--allow-checked' in args
    errors, warns = [], []

    design = (out / 'DESIGN.md').read_text()
    dh = hexes(design)
    files = sorted(out.glob('00-*.md')) + sorted(out.glob('02-*.md'))
    glob = None
    for f in files:
        for b in code_blocks(f.read_text()):
            if MARK in b:
                glob = b.strip(); break
        if glob: break
    if not glob:
        sys.exit('ERROR: Global Prompt not found (looking for the phrase "%s")' % MARK)
    gh = hexes(glob)
    if dh - gh: errors.append(f'DESIGN.md hex missing from Global Prompt: {sorted(dh - gh)}')
    if gh - dh: errors.append(f'Global Prompt hex not in DESIGN.md: {sorted(gh - dh)}')

    for f in files:
        t = f.read_text()
        extra = hexes(t) - dh
        if extra: errors.append(f'{f.name}: hex not in DESIGN.md: {sorted(extra)}')
        if '{{' in t: errors.append(f'{f.name}: leftover placeholder')
        if MARK in t and glob not in t: errors.append(f'{f.name}: Global Prompt differs from the master copy')
        if not allow_checked and '[x]' in t: errors.append(f'{f.name}: contains checked boxes [x]')
        long = []
        for b in code_blocks(t):
            if b.strip() == glob or b.startswith('Screen: Design System Board'): continue
            w = len(b.split())
            if w > max_words: long.append((w, b[:50].replace('\n', ' ')))
        if long: warns.append(f'{f.name}: prompts over {max_words} words: {long}')
        n = len([b for b in code_blocks(t) if b.strip() != glob])
        print(f'{f.name}: {n} prompt blocks, {t.count("[ ]")} unchecked')

    for w in warns: print('WARN ', w)
    for e in errors: print('ERROR', e)
    print('OK' if not errors else f'{len(errors)} error(s)')
    sys.exit(1 if errors else 0)

if __name__ == '__main__':
    main()
