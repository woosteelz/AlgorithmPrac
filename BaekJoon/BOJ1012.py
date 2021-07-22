# 백준 문제번호 1012번 유기농 배추

# 중복방문을 제거하는 편이 시간효율에서 좋다.
import sys
from collections import deque

TC = int(sys.stdin.readline())

for _ in range(TC):
	M, N, K = map(int, sys.stdin.readline().split())
	ground = [[0 for _ in range(M)] for _ in range(N)]
	visited = [[False for _ in range(M)] for _ in range(N)]
	for _ in range(K):
		j, i = map(int, sys.stdin.readline().split())
		ground[i][j] = 1
	
	dir_x = [1, -1, 0, 0]
	dir_y = [0, 0, 1, -1]

	def check_bea(i, j):
		queue = deque()
		queue.append([i, j])
		visited[i][j] = True
		while queue:
			x, y = queue.popleft()
			for i in range(4):
				temp_x = x + dir_x[i]
				temp_y = y + dir_y[i]
				if 0 <= temp_x < N and 0 <= temp_y < M and ground[temp_x][temp_y] == 1 and not visited[temp_x][temp_y]:
					queue.append([temp_x, temp_y])
					visited[temp_x][temp_y] = True
	cnt = 0
	for i in range(N):
		for j in range(M):
			if not visited[i][j] and ground[i][j] == 1:
				check_bea(i, j)
				cnt += 1
	print(cnt)