# BOJ 1707번 이분 그래프
# 분리되어 있는 그래프를 생각하여야 한다!
import sys
from collections import deque
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
	V, E = map(int, input().split())
	visited = ['' for _ in range(V+1)]
	graph = [[] for _ in range(V+1)]
	for _ in range(E):
		a, b = map(int, input().split())
		graph[a].append(b)
		graph[b].append(a)
	
	def BFS(i):
		queue = deque()
		queue.append(i)
		visited[i] = 'R'
		while queue:
			curr = queue.popleft()
			for g in graph[curr]:
				if not visited[g]:
					if visited[curr] == 'B':
						visited[g] = 'R'
					elif visited[curr] == 'R':
						visited[g] = 'B'
					queue.append(g)

	for i in range(1, V+1):
		if not visited[i]:
			BFS(i)
	
	flag = False
	for i in range(1, V+1):
		for g in graph[i]:
			if visited[g] == visited[i]:
				flag = True
				break
		if flag:
			break

	print('NO' if flag else 'YES')