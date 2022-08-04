#!/usr/bin/env python

import sys


s = ""
while True:
    c = sys.stdin.read(1)
    if not c:
        break

    # sys.stdin.read normalizes line endings(?)
    if c == "\n":
        if s == "EOF":
            break
        print("sentence:", s)
        sys.stdout.flush()
        s = ""
    else:
        s += c
