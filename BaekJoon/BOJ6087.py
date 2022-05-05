from collections import deque


dir_x = [0, 1, -1, 0]
dir_y = [1, 0, 0, -1]

W, H = map(int, input().split())
graph = [list(input()) for _ in range(H)]
pos = []
for i in range(H):
    for j in range(W):
        if graph[i][j] == 'C':
            pos.append([i, j])

start = pos[0]
end = pos[1]

visited = [[float('inf') for _ in range(W)] for _ in range(H)]
visited[start[0]][start[1]] = 0
queue = deque()
queue.append(start)

while queue:
    x, y = queue.popleft()
    if end == [x, y]:
        print(visited[x][y] - 1)
        break

    for i in range(4):
        next_x, next_y = x + dir_x[i], y + dir_y[i]
        while True:
            if not (0 <= next_x < H and 0 <= next_y < W):
                break
            if graph[next_x][next_y] == '*':
                break
            if visited[next_x][next_y] < visited[x][y] + 1:
                break
            queue.append([next_x, next_y])
            visited[next_x][next_y] = visited[x][y] + 1
            next_x += dir_x[i]
            next_y += dir_y[i]
