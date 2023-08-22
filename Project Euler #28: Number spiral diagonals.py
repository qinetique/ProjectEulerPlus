# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #28: Number spiral diagonals
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler028/problem?isFullScreen=true

dick = 10 ** 9 + 7


def virgin(n):
    if n == 1:
        return 1
    s = 1
    v = (n - 1) // 2
    s += (n * (n + 1) * (2 * n + 1) // 6 - 1 - 4 * (v * (v + 1) * (2 * v + 1) // 6)) * 4 - 6 * v * (v + 1)
    return s


t = int(input())
for i in range(t):
    n = int(input())
    print(virgin(n) % dick)
