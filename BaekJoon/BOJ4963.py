# BOJ 4963번 섬의 개수
import sys
from collections import deque
input = sys.stdin.readline

while True:
	a, b = map(int, input().split())
	if not a and not b:
		break
	
	graph = [list(map(int, input().split())) for _ in range(b)]
	visited = [[False for _ in range(a)] for _ in range(b)]

	dir_x = [-1, -1, -1, 0, 0, 1, 1, 1]
	dir_y = [-1, 0, 1, -1, 1, -1, 0, 1]
	
	def BFS(x, y):
		queue = deque()
		queue.append([x, y])
		visited[x][y] = True
		while queue:
			curr_x, curr_y = queue.popleft()
			for i in range(8):
				next_x = curr_x + dir_x[i]
				next_y = curr_y + dir_y[i]
				if 0<=next_x<b and 0<=next_y<a and not visited[next_x][next_y] and graph[next_x][next_y]:
					queue.append([next_x, next_y])
					visited[next_x][next_y] = True

	cnt = 0
	for i in range(b):
		for j in range(a):
			if not visited[i][j] and graph[i][j]:
				BFS(i, j)
				cnt += 1
	print(cnt)