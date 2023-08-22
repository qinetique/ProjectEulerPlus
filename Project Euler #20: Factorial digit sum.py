# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #20: Factorial digit sum
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler020/problem?isFullScreen=true

from math import factorial
t = int(input())
for i in range(t):
    n = int(input())
    f = 1
    for j in range(1, n+1):
        f *= j
    total = 0
    while f > 0:
        s = f % 10
        total += s
        f = f // 10
    print(total)