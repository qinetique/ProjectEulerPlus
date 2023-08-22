# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #3: Largest prime factor
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler003/problem?isFullScreen=true

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = num = int(input().strip())
    l = 2
    while not num % 2:
        num //= 2
    f = 3
    mf = num ** 0.5
    while f <= mf:
        if not num % f:
            l = f
            num //= f
            while not num % f:
                num //= f
            if num == 1:
                print(l)
                break
            mf = num ** 0.5
        f += 2
    else:
        print(num)
