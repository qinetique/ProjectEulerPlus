# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #7: 10001st prime
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true
from math import ceil, log

# !/bin/python3

max_bound = 10 ** 4 + 1
l = ceil(max_bound * (log(max_bound) + log(log(max_bound))))

# import sys

l += 1  # needed function?
num = [True] * l
p = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if len(p) >= n:
        print(p[n - 1])
        continue
    for i in range(next(reversed(p), 1) + 1, l):
        if num[i]:
            p.append(i)
            for j in range(i * i, l, i):
                num[j] = False
            if len(p) == n:
                print(i)
                break
