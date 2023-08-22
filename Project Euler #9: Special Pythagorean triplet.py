# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #9: Special Pythagorean triplet
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem?isFullScreen=true

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    l = -1
    for i in range(1, n//3+1):
        j = n * (i - n // 2) // (i - n)
        k = n - i - j
        if i*i+j*j == k*k:
            p = i*j*k
            if p > l:
                l = p
    print(l)