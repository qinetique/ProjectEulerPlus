# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #35: Circular primes
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler035/problem?isFullScreen=true

def prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


def circular(n):
    c = str(n)
    l = []
    for i in range(len(c)):
        rotation = c[i:] + c[:i]
        l.append(int(rotation))
    for j in l:
        if not prime(j):
            return False
    return True

n = int(input())
d = {10:17}
s = 17
for i in range(10,10**6+1):
    d[i] = s
    if circular(i):
        s += i
print(d[n])
