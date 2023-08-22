# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #23: Non-abundant sums
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler023/problem?isFullScreen=true
import math


def non_abundant_sum(n):
    sm = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            sm += i
            x = n / i
            if i != x:
                sm += x
    return sm + 1


l = [0, 0]

for i in range(2, 28123):
    if i < non_abundant_sum(i):
        l.append(1)
    else:
        l.append(0)

t = int(input())
for _ in range(t):
    p = int(input())
    if p > 28122:
        print("YES")
    else:
        for i in range(1, p // 2 + 1):
            if l[p - i] and l[i]:
                print("YES")
                break
        else:
            print("NO")
