from collections import deque

def DFS(graph, V, visited):
  visited[V] = True
  print(V, end = ' ')
  for i in graph[V]:
    if not visited[i]:
      DFS(graph, i, visited)

def BFS(graph, V, visited):
  queue = deque()
  queue.append(V)
  visited[V] = True
  while queue:
    v = queue.popleft()
    print(v, end = ' ')
    for i in graph[v]:
      if not visited[i]:
        queue.append(i)
        visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for g in graph:
  g.sort()

print(graph)

visited = [False] * (N+1)
DFS(graph, V, visited)
print()
visited = [False] * (N+1)
BFS(graph, V, visited)