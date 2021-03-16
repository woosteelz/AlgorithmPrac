# 백준 문제번호 2178번 미로 탐색
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
info = []
visited = [[False for _ in range(M)] for _ in range(N)]
print(visited)
for _ in range(N):
	info.append(list(map(int, sys.stdin.readline().split())))

stack = deque()
stack.append((0, 0))

while True:
	temp = stack[-1]
	if stack[-1][0] == N-1 and stack[-1][1] == M-1:
		break
	elif info[temp[0]+1][temp[1]] or info[temp[0]][temp[1]+1]:
		if map[temp[0]+1][temp[1]]:
			stack.append((temp[0]+1, temp[1]))
		if map[temp[0]][temp[1]+1]:
			stack.append((temp[0], temp[1]+1))
	else:
		
