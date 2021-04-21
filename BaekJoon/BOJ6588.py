# BOJ 6588번 골드바흐의 추측
import sys

# 에리토스테네스의 체
num = 1000000
prime = [True] * (num+1)
m = int(num**0.5)
for i in range(2, m+1):
	if prime[i]:
		for j in range(i*2, num+1, i):
			prime[j] = False

while True:
	n = int(sys.stdin.readline())
	if not n:
		break

	for i in range(2, n):
		if prime[i] and prime[n-i]:
			print(n, '=', i, '+', n-i)
			break
	else:
		print('''"Goldbach's conjecture is wrong."''')