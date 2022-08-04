#!/usr/bin/env python

import sys
import time


for i in range(1, 6):
    print("x" * i)
    sys.stdout.flush()
    time.sleep(0.5)

print("EOF")
