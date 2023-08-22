# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #11: Largest product in a grid
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem?isFullScreen=true

# !/bin/python3
from functools import reduce
from operator import mul

grid = [[0] * 23] * 3
for i in range(20):
    grid.append(list(map(int, input().split())) + [0] * 3)
grid.extend([[0] * 23] * 3)
print(max(reduce(mul, [grid[r + d[0] * ofs][c+d[1] * ofs] for ofs in range(4)]) for d in ((0,1), (1,0), (1,1), (-1,1)) for r in range(3,23) for c in range(20)))