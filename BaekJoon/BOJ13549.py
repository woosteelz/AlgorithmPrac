# BOJ 13549번 숨바꼭질3
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
visited = [0] * 100001
queue = deque()
queue.append(n)
visited[n] = 1

while queue:
	curr = queue.popleft()
	if visited[k]:
		print(visited[k]-1)
		break
	
	# 3. 순간이동
	if curr*2<=100000 and not visited[curr*2]:
		visited[curr*2] = visited[curr]
		queue.appendleft(curr*2)
	# 1. 한칸 뒤로
	if 0<= curr-1 and not visited[curr-1]:
		visited[curr-1] = visited[curr] + 1
		queue.append(curr-1)
	# 2. 한칸 앞으로
	if curr+1<=100000 and not visited[curr+1]:
		visited[curr+1] = visited[curr] + 1
		queue.append(curr+1)