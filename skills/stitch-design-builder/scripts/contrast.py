#!/usr/bin/env python3
"""WCAG contrast and weekday check.

Usage: python contrast.py '#FG' '#BG' ['#FG2' '#BG2' ...] [--date YYYY-MM-DD ...]
Pairs are (foreground, background) in order. Prints the ratio and PASS/FAIL against 4.5 (text) and 3.0 (large/non-text).
"""
import datetime, sys

def lum(h):
    h = h.lstrip('#'); c = [int(h[i:i+2], 16) / 255 for i in (0, 2, 4)]
    f = lambda v: v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])

def ratio(a, b):
    la, lb = lum(a), lum(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

def main():
    args = sys.argv[1:]
    dates = []
    if '--date' in args:
        i = args.index('--date'); dates = args[i + 1:]; args = args[:i]
    if len(args) % 2:
        sys.exit(__doc__)
    for fg, bg in zip(args[::2], args[1::2]):
        r = ratio(fg, bg)
        print(f'{r:5.2f}:1  {fg} on {bg}  text={"PASS" if r >= 4.5 else "FAIL"}  large/non-text={"PASS" if r >= 3 else "FAIL"}')
    for d in dates:
        print(d, datetime.date.fromisoformat(d).strftime('%A'))

if __name__ == '__main__':
    main()
