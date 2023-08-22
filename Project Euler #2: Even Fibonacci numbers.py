# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #2: Even Fibonacci numbers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem?isFullScreen=true

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # need 3 ints
    p, q , r = 1, 2, 3
    ev_total = 2
    while r < n :
        if not r % 2:
            ev_total += r
        p, q, r = q, r, q + r
    print(ev_total)