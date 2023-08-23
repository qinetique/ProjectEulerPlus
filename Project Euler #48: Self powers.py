# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #48: Self powers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler048/problem?isFullScreen=true

def self_power(num, p, m):
    res = 1
    while p:
        if p % 2:
            res = (res * num) % m
        p //= 2
        num = (num ** 2) % m
    return res


n = int(input())
res = 0
for i in range(1, n + 1):
    res += self_power(i, i, 10 ** 10)
print(res % (10 ** 10))
