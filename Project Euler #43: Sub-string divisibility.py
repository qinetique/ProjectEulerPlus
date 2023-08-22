# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #43: Sub-string divisibility
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler043/problem?isFullScreen=true
from itertools import permutations


def divs(n):
    sp = []
    for i in permutations(range(0, n + 1)):
        s = ''.join(map(str, i))
        sp.append(s)
    total = 0
    for s in sp:
        if len(s[1:4]) == 3:
            if int(s[1:4]) % 2 == 0:
                pass
            else:
                continue
        else:
            pass
        if len(s[2:5]) == 3:
            if int(s[2:5]) % 3 == 0:
                pass
            else:
                continue
        else:
            pass
        if len(s[3:6]) == 3:
            if int(s[3:6]) % 5 == 0:
                pass
            else:
                continue
        else:
            pass
        if len(s[4:7]) == 3:
            if int(s[4:7]) % 7 == 0:
                pass
            else:
                continue
        else:
            pass
        if len(s[5:8]) == 3:
            if int(s[5:8]) % 11 == 0:
                pass
            else:
                continue
        else:
            pass
        if len(s[6:9]) == 3:
            if int(s[6:9]) % 13 == 0:
                pass
            else:
                continue
        else:
            pass
        if len(s[7:10]) == 3:
            if int(s[7:10]) % 17 == 0:
                pass
            else:
                continue
        else:
            pass
        total += int(s)
    return total


if __name__ == '__main__':
    n = int(input())
    print(divs(n))
