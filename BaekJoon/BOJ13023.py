# BOJ 13023번 ABCDE
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
for _ in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

flag = False
visited = [False for _ in range(n)]

def DFS(node, depth):
	global flag
	visited[node] = True
	if depth >= 4:
		flag = True
		return
	for next in graph[node]:
		if not visited[next]:
			visited[next] = True
			DFS(next, depth+1)
			visited[next] = False

for i in range(n):
	DFS(i, 0)
	visited[i] = False
	if flag:
		break
print(1 if flag else 0)