# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #31: Coin sums
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler031/problem?isFullScreen=true

m = 10 ** 5
d = 10 ** 9 + 7
mm = [1, 2, 5, 10, 20, 50, 100, 200, ]
l = []
for i in range(m + 1):
    l.append(i // 2 + 1)
for i in mm[2:]:
    for j in range(m - i + 1):
        l[j + i] += l[j]

t = int(input())
for i in range(t):
    n = int(input())
    print(l[n] % d)
