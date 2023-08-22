# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #21: Amicable numbers
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler021/problem?isFullScreen=true

m_size = 10**5+1
sum_div = [1 for _ in range(m_size + 1)]
sum_div[0] = 0
sum_div[1] = 0
for i in range(2, m_size):
    for j in range(2*i, m_size, i):
        sum_div[j] += i

amicable = [0 for i in range(m_size)]
run = 0

for i in range(1, m_size):
    v = sum_div[i]
    if v < len(sum_div) and v != i:
        if sum_div[v] == i:
            run += i
    amicable[i] = run

t = int(input())
for i in range(t):
    n = int(input())
    print(amicable[n - 1])
