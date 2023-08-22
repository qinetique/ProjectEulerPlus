# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #30: Digit Nth powers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler030/problem?isFullScreen=true

def cal(n, p):
    total = 0
    for i in str(n):
        total += int(i) ** p
    return total


lst = []
for j in range(3, 6):
    v = 2
    while True:
        if 9 ** j * v < 10 ** (v - 1):
            break
        v += 1
    lst.append((j, 9 ** j * (v - 1)))

r = {}
for m in lst:
    tx = 0
    for k in range(2, m[1] + 1):
        if cal(k, m[0]) == k:
            tx += k
    r[m[0]] = tx
n = int(input())
print(r[n])
