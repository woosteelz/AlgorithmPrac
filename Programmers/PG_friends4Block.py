# 프로그래머스 프렌즈4블록(Level 2)
from collections import deque

def solution(m, n, board):
	answer = 0
	
	for i in range(m):
		board[i] = list(board[i])

	while True:
		visited = [[0 for _ in range(n)] for _ in range(m)]
		for i in range(m-1):
			for j in range(n-1):
				if board[i][j] == board[i+1][j] == board[i][j+1]== board[i+1][j+1] and board[i][j] != '-':
					visited[i][j] = 1
					visited[i][j+1] = 1
					visited[i+1][j] = 1
					visited[i+1][j+1] = 1
		out = True
		for i in range(m):
			for j in range(n):
				if visited[i][j]:
					out = False
					answer += 1
					board[i][j] = '-'
		if out:
			break
		while True:
			flag = True
			for i in range(1, m):
				for j in range(n):
					if board[i][j] == '-' and board[i-1][j] != '-':
						flag = False
						board[i-1][j], board[i][j] = board[i][j], board[i-1][j]
			if flag:
				break

	return answer

print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))