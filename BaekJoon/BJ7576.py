# 백준 문제번호 7576번 토마토

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatos = []
for _ in range(N):
	tomatos.append(list(map(int, sys.stdin.readline().split())))
queue = deque()

for i in range(N):
	for j in range(M):
		if tomatos[i][j] == 1:
			queue.append([i, j])

dir_x = [1, -1, 0, 0]
dir_y = [0, 0, -1, 1]

while queue:
	x, y = queue.popleft()
	for i in range(4):
		temp_x = x + dir_x[i]
		temp_y = y + dir_y[i]
		if 0 <= temp_x < N and 0 <= temp_y < M:
			if not tomatos[temp_x][temp_y]:
				tomatos[temp_x][temp_y] = 1 + tomatos[x][y]
				queue.append([temp_x, temp_y])
ans = 0
for t in tomatos:
	if 0 in t:
		print(-1)
		break
	if ans < max(t):
		ans = max(t)
else:
	print(ans-1)