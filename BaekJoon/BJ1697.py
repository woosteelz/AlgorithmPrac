# 백준 문제번호 1697번 숨바꼭질

import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
visited = [False for _ in range(100001)]
queue = deque()

queue.append([N, 0])

while queue:
	curr, cnt = queue.popleft()
	visited[curr] = True
	if curr == K:
		print(cnt)
		break
	
	if curr - 1 >= 0 and not visited[curr-1]:
		queue.append([curr-1, cnt+1])
	if curr + 1 <= 100000 and not visited[curr+1]:
		queue.append([curr+1, cnt+1])
	if curr * 2 <= 100000 and not visited[curr*2]:
		queue.append([curr*2, cnt+1])
		
