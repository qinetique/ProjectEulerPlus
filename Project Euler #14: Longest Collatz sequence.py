# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #14: Longest Collatz sequence
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler014/problem?isFullScreen=true

# Time : O(NlogN)?

N = 5 * (10 ** 6)
c = [0 for i in range(N+1)]
c[1] = 1
c[2] = 2


def mem(n):
    if n <= N:
        return c[n]
    return 0


def sec_mem(n, co):
    if n <= N:
        c[n] = co


def th_mem(n):
    p = n
    co = 0
    ln = []
    while p != 1:
        var = mem(p)
        if var == 0:
            ln.append(p)
            co += 1
        else:
            break
        if p % 2 == 0:
            p = p // 2
        else:
            p = 3 * p + 1
    for r in ln:
        sec_mem(r, var + co)
        co -= 1


for i in range(3, N + 1):
    th_mem(i)

mx = [0 for i in range(N+1)]
mv = 0
mn = 0
for i in range(1, N+1):
    if c[i] >= mv:
        mx[i] = i
        mv = c[i]
    else:
        mx[i] = mx[i - 1]

T = int(input())
for i in range(T):
    N = int(input())
    print(mx[N])