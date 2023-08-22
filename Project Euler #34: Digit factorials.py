# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #34: Digit factorials
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler034/problem?isFullScreen=true
import math


def digit_fact(num):
    if sum([math.factorial(int(a)) for a in str(num)]) % num == 0:
        return True
    else:
        return False


n = int(input())
res = 0
for i in range(10, n):
    if digit_fact(i):
        res += i
print(res)
