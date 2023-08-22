# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #12: Highly divisible triangular number
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler012/problem?isFullScreen=true
#from distlib.compat import raw_input


def div(num, p):
    div_count = 1
    f = num
    for i in range(0, len(p)):
        if p[i]**2 > f:
            return div_count * 2
        count = 1
        while f % p[i] == 0:
            count += 1
            f = f / p[i]
        div_count *= count
        if f == 1:
            return div_count
    return div_count


x = [True]*(10**4)
p = []
for a in range(2, 10**2):
    if x[a] == True:
        p.append(a)
        for b in range(a*a, 10**4, a):
            x[b] = False
for a in range(10**2, 10**4):
    if x[a] == True:
        p.append(a)

t = int(input())
for i in range(0, t):
    n = int(input())
    count = 2
    div_count = 0
    od = 1
    ev = 1

    while div_count <= n:
        if count % 2 == 0:
            ev = div(count+1, p)
            div_count = ev*od
        else:
            od = div((count+1)/2, p)
            div_count = ev*od
        count += 1
    res = int(count*(count - 1)/2)
    print(res)
