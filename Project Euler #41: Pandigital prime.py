# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #41: Pandigital prime
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler041/problem?isFullScreen=true

import itertools


def isprime(n):
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


pd = []
for i in range(1, 10):
    pd += [int(''.join(a)) for a in itertools.permutations([str(n) for n in range(1, i + 1)]) if
           isprime(int(''.join(a)))]

for _ in range(int(input())):
    n = int(input())
    res = -1
    for i in pd[::-1]:
        if i <= n:
            res = i
            break
    print(res)
