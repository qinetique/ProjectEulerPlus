# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #39: Integer right triangles
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler039/problem?isFullScreen=true
import itertools
import math

n = 5 * 10 ** 6
res = [0] * (n + 1)
for m in itertools.combinations(range(1, int(n ** 0.5) + 1, 2), r=2):
    t = m[0]
    s = m[1]
    if math.gcd(s, t) == 1:
        for i in range(s * (s + t), n + 1, s * (s + t)):
            res[i] += 1

mx = 0
sr = 0
final_res = []
for i in range(0, n + 1):
    var = res[i]
    if var > mx:
        sr = i
        mx = var
    final_res.append(sr)

t = int(input())
for j in range(t):
    n = int(input())
    print(final_res[n])
