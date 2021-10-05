from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
dist = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(n-1):
    a, b, d = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    dist[a][b] = d
    dist[b][a] = d

queue = deque()

for _ in range(m):
    visited = [False for _ in range(n+1)]
    start, end = map(int, input().split())
    visited[start] = True
    queue.append(start)
    ans = [0 for _ in range(n+1)]
    while queue:
        curr = queue.popleft()
        for node in graph[curr]:
            if not visited[node]:
                queue.append(node)
                ans[node] += dist[curr][node] + ans[curr]
                visited[node] = True
    print(ans[end])
