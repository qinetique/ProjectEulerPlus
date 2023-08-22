# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #16: Power digit sum
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler016/problem?isFullScreen=true

def pw_total(n):
    total = 0
    for i in str(n):
        total += int(i)
    return total


t = int(input())
for i in range(t):
    n = int(input())
    print(pw_total(2**n))