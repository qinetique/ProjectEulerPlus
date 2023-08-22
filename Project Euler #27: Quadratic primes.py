# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #27: Quadratic primes
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler027/problem?isFullScreen=true
import itertools


def prime(v):
    if v % 2 == 0:
        return False
    for i in range(3, int(v ** 0.5) + 1, 2):
        if v % i == 0:
            return False
    return True


n = int(input())
madarchod_math = 0
dhon = []
# list, neg(-) value = ?
for i in itertools.product(list(range(-n, n + 1, 1)), range(n + 1)):
    ps = 0
    gud = 0
    while True:
        sex = gud ** 2 + i[0] * gud + i[1]
        if sex < 0:
            break
        if not prime(sex):
            break
        gud += 1
        ps += 1
    if ps > madarchod_math:
        dhon.append(i)
        madarchod_math = ps
print(*dhon[-1])
