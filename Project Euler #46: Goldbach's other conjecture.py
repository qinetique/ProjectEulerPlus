# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #46: Goldbach's other conjecture
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler046/problem?isFullScreen=true

def fun(n):
    res = set()
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            res.add(p)
    return res


ps = fun(5 * 10 ** 5)
sq = [2 * x * x for x in range(5 * 10 ** 2)]

t = int(input())
for i in range(t):
    num = int(input())
    w = 0
    for y in sq:
        if y > num:
            break
        if (num - y) in ps:
            w += 1
    print(w)
