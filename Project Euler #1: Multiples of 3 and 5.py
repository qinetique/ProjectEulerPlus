# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #1: Multiples of 3 and 5
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem?isFullScreen=true

#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    mul_3 = (n - 1) // 3
    mul_5 = (n - 1) // 5
    mul_15 = (n - 1) // 15
    total = (3 * mul_3 * (mul_3 + 1) // 2 + 5 * mul_5 * (mul_5 + 1) // 2 - 15 * mul_15 * (mul_15 + 1) // 2)
    print(total)