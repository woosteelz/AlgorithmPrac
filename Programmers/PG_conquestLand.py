# 프로그래머스 땅따먹기 (Level 2)
from collections import deque

def solution(land):
	answer = []
	arr = [[0, 0, 0, 0] for _ in range(len(land))]
	arr = land
	for i in range(1, len(land)):
		for n in range(4):
			curr = land[i][n]
			for m in range(4):
				if n == m:
					pass
				else:
					if curr + land[i-1][m] > arr[i][n]:
						arr[i][n] = curr + land[i-1][m]
	
	return max(arr[-1])
					


land = [[4, 3, 2, 1], [2, 2, 2, 1], [6, 6, 6, 4], [8, 7, 6, 5]]
print(solution(land))