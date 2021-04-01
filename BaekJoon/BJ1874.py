# 백준 1874번 스택 수열
import sys

n = int(sys.stdin.readline())
arr = []
for _ in range(n):
	arr.append(int(sys.stdin.readline()))
stack = []
answer = []
i = 1
while stack or i <= n:
	if not stack:
		stack.append(i)
		answer.append('+')
		i += 1
	elif arr[0] == stack[-1]:
		stack.pop(-1)
		arr.pop(0)
		answer.append('-')
	elif i <= n:
		stack.append(i)
		answer.append('+')
		i += 1
	else:
		break

if arr:
	print('NO')
else:
	for i in answer:
		print(i)