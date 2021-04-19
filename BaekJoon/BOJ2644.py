# BOJ 2644번 촌수계산
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
x, y = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
	a, b = map(int, input().split())
	graph[a].append(b)
	graph[b].append(a)

stack = deque()
visited = [False for _ in range(n+1)]
stack.append(x)
visited[x] = True
chon = 0
flag = True
while stack and flag:
	curr = stack[-1]
	for node in graph[curr]:
		if not visited[node]:
			stack.append(node)
			visited[node] = True
			chon += 1
			if node == y:
				print(chon)
				flag = False
			break
	else:
		stack.pop()
		chon -= 1
if x == y:
	print(0)
elif flag:
	print(-1)