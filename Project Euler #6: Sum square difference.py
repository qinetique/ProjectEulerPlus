# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #6: Sum square difference
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    sq = (n*(n+1)//2)**2
    ss = (n*(n+1)*(2*n+1)//6)
    print(sq-ss)