# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #29: Distinct powers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler029/problem?isFullScreen=true

def power(n: int) -> int:
    count = 0
    tst = [0] * (n + 1)
    for i in range(2, n + 1):
        if tst[i]:
            continue
        c = set()
        p = 2
        while i ** p <= n:
            tst[i ** p] = True
            s = set([j * p for j in range(2, n + 1) if j * p > n])
            c.update(s)
            p += 1
        count += len(c) + n - 1
    return count


t = int(input())
print(power(t))
