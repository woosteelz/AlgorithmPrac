# 프로그래머스 N으로 표현 (Level 3)
import sys
from collections import deque

def solution(n, computers):
	visited = [False for _ in range(n)]
	graph = [[0] for _ in range(n)]
	for i in range(n):
		for j in range(n):
			if i == j:
				pass
			else:
				if computers[i][j]:
					graph[i].append(j)

	print(graph)

	def check(k):
		queue = deque()
		queue.append(k)
		visited[k] = True
		while queue:
			temp = queue.popleft()
			for g in graph[temp]:
				if not visited[g]:
					visited[g] = True
					queue.append(g)

	cnt = 0
	for i in range(n):
		if not visited[i]:
			check(i)
			cnt += 1

	return cnt

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
