# 백준 문제번호 9095번 1, 2, 3 더하기

import sys

arr = [1, 2, 4]
for i in range(3, 10):
	arr.append(arr[i-3]+arr[i-2]+arr[i-1])

TC = int(sys.stdin.readline())

for _ in range(TC):
	N = int(sys.stdin.readline())
	print(arr[N-1])
