# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #33: Pandigital multiples
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler038/problem?isFullScreen=true

def pandigital(n, k):
    i = 1
    num = ''
    while True:
        num += str(n * i)
        if len(num) >= k:
            break
        i += 1
    if len(num) == k:
        if set([str(x) for x in range(1, k + 1)]).issubset(num):
            return True
    return False


m = input().split()
n = int(m[0])
k = int(m[1])

for i in range(2,n):
    if pandigital(i, k):
        print(i)