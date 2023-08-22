# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #22: Names scores
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler022/problem?isFullScreen=true

n = int(input())
l = []
for i in range(n):
    name = input()
    l.append(name)
l.sort()
m = {}
for i in range(1, n + 1):
    name = l[i - 1]
    total = 0
    for v in name:
        total = total + ord(v) - 64
    total *= i
    m[name] = total
q = int(input())
for i in range(q):
    name = input()
    print(m[name])