# Author : Tonmoy M
# Author URI: https://qinetique.github.io
# Problem : Project Euler #49: Prime permutations
# Problem Domain: HackerRank
# Problem URI: https://www.hackerrank.com/contests/projecteuler/challenges/euler049/problem?isFullScreen=true

def is_prime(v):
    if v % 2 == 0:
        return False
    for i in range(3, int(v ** 0.5) + 1, 2):
        if v % i == 0:
            return False
    return True


def are_permutations(p, q):
    return sorted(str(p)) == sorted(str(q))


def permutation_sequences(N, K):
    result = []
    for num in range(1000, N):
        if is_prime(num):
            sequence = [num]
            for i in range(1, K):
                next_num = num + i * 3330
                if is_prime(next_num) and are_permutations(num, next_num):
                    sequence.append(next_num)
                else:
                    break
            if len(sequence) == K:
                result.append(sequence)
    return result


def main():
    N, K = map(int, input().split())
    sequences = permutation_sequences(N, K)
    for sequence in sequences:
        concatenated = int(''.join(map(str, sequence)))
        print(concatenated)


if __name__ == "__main__":
    main()
