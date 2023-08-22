# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #10: Summation of primes
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler010/problem?isFullScreen=true
from math import sqrt
from bisect import bisect

l = 2_000_000

p = []
sum = [0]
var = [True] * l
for i in range(2, int(sqrt(l))):
    if var[i]:
        p.append(i)
        sum.append(sum[-1] + i)
        for j in range(i * i, l, i):
            var[j] = False
for i in range(int(sqrt(l)), l):
    if var[i]:
        p.append(i)
        sum.append(sum[-1] + i)
# !/bin/python3

# import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ind = bisect(p, n)
    print(sum[ind])
