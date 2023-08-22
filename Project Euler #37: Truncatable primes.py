# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #37: Truncatable primes
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler037/problem?isFullScreen=true

mx = 10 ** 6 + 1
nums = [True] * (mx)


def truncatable(n):
    s = str(n)
    t = s[::-1]
    return all((nums[int(s[:j])] and nums[int(t[:j][::-1])] for j in range(1, len(s) + 1)))


def func():
    # global nums
    nums[0] = nums[1] = False
    for i in range(2, mx):
        if i * i > mx - 1:
            break
        for j in range(i * i, mx, i):
            nums[j] = False


def main():
    func()
    total = 0
    n = int(input())
    for i in range(11, n, 2):
        if nums[i]:
            if truncatable(i):
                total += i
    print(total)


if __name__ == '__main__':
    main()
