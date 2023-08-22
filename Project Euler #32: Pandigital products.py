# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #32: Pandigital products
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler032/problem?isFullScreen=true

n = int(input())
o = [i for i in range(1, n + 1)]
a = 0
b = 0
c = 0
sol = set()
for i in range(1, 10 ** 2):
    for j in range(1, 10 ** 4):
        if i == j:
            continue
        res = i * j
        t = str(i) + str(j) + str(res)
        t = list(map(int, t))
        t = sorted(t)
        if t == o:
            sol.add(res)
print(sum(sol))
