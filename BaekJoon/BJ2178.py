# 백준 문제번호 2178번 미로 탐색
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
info = []
for _ in range(N):
	info.append(list(sys.stdin.readline()))

dir_x = [1, 0,-1, 0]
dir_y = [0, 1, 0, -1]

queue = deque()
queue.append([0, 0])
info[0][0] = 1
while queue:
	x, y = queue.popleft()
	for i in range(4):
		temp_x = x + dir_x[i]
		temp_y = y + dir_y[i]
		if 0 <= temp_x < N and 0 <= temp_y < M and info[temp_x][temp_y] == '1':
			queue.append([temp_x, temp_y])
			info[temp_x][temp_y] = 1 + info[x][y]

print(info[N-1][M-1])