# 백준 1929번 소수 구하기
import sys
import math

M, N = map(int, sys.stdin.readline().split())

def get_prime_nums(n):
    prime = [True] * (n+1)

    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i + i, n+1, i):
                prime[j] = False

    return prime

got_prime = get_prime_nums(N)
got_prime[1] = False

for i in range(M, N+1):
	if got_prime[i]:
		print(i)