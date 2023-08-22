# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #44: Pentagon numbers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler045/problem?isFullScreen=true

m = input().split()
k = int(m[1])
n = int(m[0])


def panty(i):
    return i * (3 * i - 1) // 2


p = set([i * (3 * i - 1) // 2 for i in range(1, n)])
for i in range(k + 1, n):
    if (panty(i) - panty(i - k) in p) or (panty(i) + panty(i - k) in p):
        print(panty(i))
