# 프로그래머스 프렌즈4블록(Level 2)
from collections import deque

def solution(n, a, b):
	answer = 0

	while a != b:
		a = (a+1) // 2
		b = (b+1) // 2
		answer += 1

	return answer

print(solution(8, 4, 7))