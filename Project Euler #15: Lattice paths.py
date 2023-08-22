# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #15: Lattice paths
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler015/problem?isFullScreen=true

# binomial Coef is failing for some test cases.
# Com with Factorial?

from math import factorial
v = 10**9+7
t = int(input())
for i in range(t):
    it = input().split()
    n = int(it[0])
    m = int(it[1])
    soln = factorial(n+m) // factorial(n) // factorial(m)
    print(soln%v)
