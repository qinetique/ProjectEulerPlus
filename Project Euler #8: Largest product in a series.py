# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #8: Largest product in a series
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem?isFullScreen=true

# !/bin/python3

import sys
from functools import reduce
from operator import mul

t = int(input())
for a0 in range(t):
    n, k = map(int, input().split())
    #n, k = [int(n), int(k)]
    num = list(map(int, input()))
    mp = p = reduce(mul, num[:k])
    for i in range(1, n - k):
        try:
            p //= num[i - 1]
            p *= num[i + k - 1]
        except:
            p = reduce(mul, num[i:i + k])
        if p > mp:
            mp = p
    print(mp)
