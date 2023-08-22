# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #25: N-digit Fibonacci number
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler025/problem?isFullScreen=true

import sys
sys.set_int_max_str_digits(6000)

l = [1, 1]
arr = [0, 1, ]
v = 2
ml = 1

while ml < 5000:
    v += 1
    num = l[-2]+l[-1]
    ln = len(str(num))
    l.append(num)
    if ln > ml:
        arr += [v] * (ln-ml)
        ml = ln

t = int(input())
for i in range(t):
    n = int(input())
    print(arr[n])