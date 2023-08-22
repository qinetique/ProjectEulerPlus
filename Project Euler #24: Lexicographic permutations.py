# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #24: Lexicographic permutations
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler024/problem?isFullScreen=true

c = False
t = int(input())
for _ in range(t):
    n = int(input()) - 1
    x = 1
    arr = []
    while n != 0:
        v = n % x
        n = n // x
        arr.insert(0, v)
        x = x + 1

    ch_arr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    if len(arr) < len(ch_arr):
        for _ in range(len(ch_arr) - len(arr)):
            arr.insert(0, 0)
    n_arr = []
    for i in arr:
        n_arr.append(ch_arr[i])
        ch_arr.pop(i)
    if c:
        print('')
    for i in n_arr:
        print(i, end='')
    c = True
