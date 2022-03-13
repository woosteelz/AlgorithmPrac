from collections import deque

n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dice = [1, 2, 3, 4, 5, 6]

dir_x = [0, 1, 0, -1]
dir_y = [1, 0, -1, 0]


def bfs(k):
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            next_x, next_y = x + dir_x[i], y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y] and graph[next_x][next_y] == k:
                cnt += 1
                visited[next_x][next_y] = True
                queue.append([next_x, next_y])
    return cnt


x, y, way, ans = 0, 0, 0, 0
for _ in range(k):
    if not 0 <= x + dir_x[way] < n or not 0 <= y + dir_y[way] < m:
        way = (way + 2) % 4

    visited = [[False for _ in range(m)] for _ in range(n)]

    x, y = x + dir_x[way], y + dir_y[way]
    visited[x][y] = True
    queue = deque()
    queue.append([x, y])

    ans += bfs(graph[x][y]) * graph[x][y]

    if way == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif way == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif way == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]

    if dice[5] > graph[x][y]:
        way = (way + 1) % 4
    elif dice[5] < graph[x][y]:
        way = (way + 3) % 4

print(ans)
