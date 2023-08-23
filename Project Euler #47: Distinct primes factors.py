# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #47: Distinct primes factors
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler047/problem?isFullScreen=true

def distinct_sieve(N):
    A = [0] * (1 + N)
    for p in range(2, 1 + N):
        if A[p]:
            continue
        for n in range(p, 1 + N, p):
            A[n] += 1
    return A


t = input().split()
for _ in range(2, 20):
    a = distinct_sieve(t)
print(a)

# solve this with cpp
