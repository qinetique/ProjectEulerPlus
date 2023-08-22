# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #36: Double-base palindromes
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler036/problem?isFullScreen=true

def rough(num, b):
    soln = ''
    while num:
        soln = str(num % b) + soln
        num = num // b
    return soln


def palindrome(n):
    n = str(n)
    if n == n[::-1]:
        return True
    else:
        return False


en = input().split()
n = int(en[0])
k = int(en[1])
res = 0
for i in range(1, n):
    if palindrome(i) and palindrome(rough(i, k)):
        res += i
print(res)
