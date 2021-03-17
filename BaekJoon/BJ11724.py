# 백준 문제번호 11724번 연결 요소의 개수
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
	u, v = map(int, sys.stdin.readline().split())
	graph[u].append(v)
	graph[v].append(u)
visited = [False for _ in range(N+1)]

queue = deque()

def check_vertex(n):
	queue.append(n)
	visited[n] = True
	while queue:
		temp = queue.popleft()
		for v in graph[temp]:
			if not visited[v]:
				queue.append(v)
				visited[v] = True

cnt = 0
for i in range(N):
	if not visited[i+1]:
		check_vertex(i+1)
		cnt += 1
print(cnt)
