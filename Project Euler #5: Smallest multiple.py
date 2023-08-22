# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #5: Smallest multiple
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem?isFullScreen=true

def gud(x, y):
    if y:
        return gud(y, x % y)
    else:
        return x
    # !/bin/python3

    # import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = 1
    for i in range(2, n+1):
        p *= i // gud(p, i)
    print(p)
