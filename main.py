# 프로그래머스 방문길이 (Level 2)

# 경로가 겹치면 안된다는 것이 핵심 >> 1, 0 -> 0, 1 == 0, 1 -> 1, 0
from collections import deque
import math

def solution(board):
	N = len(board)
	M = len(board[0])
	for i in range(1, N):
		for j in range(1, M):
			if board[i][j]:
				board[i][j] += min(board[i-1][j-1], board[i][j-1], board[i-1][j])
	ans = max(board[0])
	for i in range(1, N):
		if ans < max(board[i]):
			ans = max(board[i])
	return ans ** 2


board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
board = [[0,0,1,1],[1,1,1,1]]
print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[1, 1, 1, 1], [0, 1, 1, 1], [0, 1, 1, 1]]))
print(solution([[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[1, 1, 1, 1, 1],[0, 0, 1, 1, 1]]))