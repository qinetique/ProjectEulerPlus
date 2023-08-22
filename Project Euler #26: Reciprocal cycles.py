# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #26: Reciprocal cycles
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler026/problem?isFullScreen=true

def reciprocalcycle(n):
    while n % 2 == 0:
        n = n // 2
    while n % 5 == 0:
        n = n // 5
    if n == 1:
        return 0
    d = 1
    rm = 1
    while True:
        rm *= 10
        rm = rm % n
        if rm == 1:
            break
        d += 1
    return d


var = [0, 0, 0, 0, ]
md = 0
for i in range(3, 10 ** 4):
    d = reciprocalcycle(i)
    if d > md:
        md = d
        num = i
    var.append(num)

t = int(input())
for i in range(t):
    n = int(input())
    print(var[n])
