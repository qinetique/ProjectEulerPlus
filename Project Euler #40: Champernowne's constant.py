# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #40: Champernowne's constant
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler040/problem?isFullScreen=true

def search(x):
    i = 1
    while True:
        x += - (9 * 10 ** (i - 1)) * i
        if x <= 0:
            x += (9 * 10 ** (i - 1)) * i
            break
        i += 1
    l = (x - 1) // i
    res = str(10 ** (i - 1) + l)[x - l * i - 1]
    return int(res)


t = int(input())
for i in range(t):
    v = 1
    n = input().split()
    for j in n:
        v *= search(int(j))
    print(v)
