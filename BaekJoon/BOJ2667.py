# 백준 문제번호 2667번 단지번호붙이기
import sys
from collections import deque

N = int(sys.stdin.readline())
info = []
for _ in range(N):
	info.append(list(sys.stdin.readline()))
visited = [[False for _ in range(N)] for _ in range(N)]

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

def check_danji(a, b):
	queue = deque()
	queue.append([a, b])
	visited[a][b] = True
	cnt = 1
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			temp_x = x + dir_x[i]
			temp_y = y + dir_y[i]
			if 0 <= temp_x < N and 0 <= temp_y < N and info[temp_x][temp_y] == '1' and not visited[temp_x][temp_y]:
				cnt += 1
				queue.append([temp_x, temp_y])
				visited[temp_x][temp_y] = True
	return cnt
ans = []
for i in range(N):
	for j in range(N):
		if info[i][j] == '1' and not visited[i][j]:
			ans.append(check_danji(i, j))
ans.sort()
print(len(ans))
for a in ans:
	print(a)