# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #42: Coded triangle numbers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler042/problem?isFullScreen=true
import math

t = int(input())
for i in range(t):
    n = int(input())
    v = math.sqrt(8*n+1)
    if v == int(v):
        print((int(v) - 1) // 2)
    else:
        print(-1)