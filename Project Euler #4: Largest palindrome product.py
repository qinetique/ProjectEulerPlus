# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #4: Largest palindrome product
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler004/problem?isFullScreen=true

#!/bin/python3

import sys

# time complexity : O(n^2)
# space complexity: O(n^2)


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # need limit ?
    l = 0
    lim = n - 1
    for i in range(999, 100, -1):
        if i % 11:
            s = min(990, lim // i // 11 * 11)
            count = -11
        else:
            s = min(999, lim // i)
            count = -1
        for j in range(s, i, count):
            p = i * j
            if p <= l:
                break
            ps = str(p)
            if ps == ps[::-1]:
                l = p
                break
    print(l)
    # l for laurha

