# 프로그래머스 가장 큰 정사각형 찾기 (Level 2)

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