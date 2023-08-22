# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #33: Digit canceling fractions
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler033/problem?isFullScreen=true
import itertools


def add_to_list(s, num):
    l = len(s[0]) + 1
    ls = [string[:i] + str(num) + string[i:] for string in s for i in range(l)]
    return ls


def sorting(v, w):
    while v:
        n = v.pop()
        w = add_to_list(w, n)
    return set(w)


def to_str(p):
    return ''.join([str(x) for x in p])


def to_int(p):
    return int(''.join([str(x) for x in p]))


m = input().split()
n = int(m[0])
k = int(m[1])

a = list(itertools.product(range(10), repeat=n - k))
a.remove((0,) * (n - k))
b = list(itertools.combinations_with_replacement(range(1, 10), r=k))
res = set()
c = []
for i in b:
    d = []
    for j in a:
        d += [(to_int(j), int(i)) for i in sorting(list(i), [to_str(j)]) if i[0] != '0']
    c.append(d)
for i in c:
    for m in itertools.combinations(i, r=2):
        if m[0][0] < m[1][0] and m[0][0]*m[1][1] == m[1][0]*m[0][1]:
            res.add((m[0][1], m[1][1]))
print(sum([z[0] for z in res]), sum([z[1] for z in res]))
