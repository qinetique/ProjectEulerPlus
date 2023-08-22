# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #18: Maximum path sum I
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler018/problem?isFullScreen=true

# time : o(n^2)

t = int(input())
for i in range(t):
    n = int(input())
    tri = []
    mx = []
    for j in range(n):
        tri.append(list(map(int, input().rstrip().split())))
        mx.append([0]*(j+1))
    for k in range(n):
        mx[n-1][k] = tri[n-1][k]
    for i in range(n-2,-1,-1):
        for j in range(i+1):
            mx[i][j] = tri[i][j] + max(mx[i+1][j], mx[i+1][j+1])
    print(mx[0][0])
