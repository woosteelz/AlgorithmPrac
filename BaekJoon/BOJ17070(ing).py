# 17070번 파이프 옮기기1
from collections import deque


def is_width(x, y):
    if x[0] == y[0] and x[1] + 1 == y[1]:
        return True
    return False


def is_length(x, y):
    if x[1] == y[1] and x[0] + 1 == y[0]:
        return True
    return False


def is_diagonal(x, y):
    if x[0] + 1 == y[0] and x[1] + 1 == y[1]:
        return True
    return False


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
queue = deque()
queue.append([(0, 0), (0, 1)])
cnt = 0

while queue:
    prev, curr = queue.popleft()

    if curr == (N-1, N-1):
        cnt += 1
        continue

    if is_width(prev, curr):

        if curr[1] + 1 < N and not graph[curr[0]][curr[1] + 1]:
            queue.append([curr, (curr[0], curr[1] + 1)])

        if curr[0] + 1 < N and curr[1] + 1 < N and not graph[curr[0] + 1][curr[1] + 1] and not graph[curr[0]][curr[1] + 1] and not graph[curr[0] + 1][curr[1]]:
            queue.append([curr, (curr[0] + 1, curr[1] + 1)])

    elif is_length(prev, curr):

        if curr[0] + 1 < N and not graph[curr[0] + 1][curr[1]]:
            queue.append([curr, (curr[0] + 1, curr[1])])

        if curr[0] + 1 < N and curr[1] + 1 < N and not graph[curr[0] + 1][curr[1] + 1] and not graph[curr[0]][curr[1] + 1] and not graph[curr[0] + 1][curr[1]]:
            queue.append([curr, (curr[0] + 1, curr[1] + 1)])

    elif is_diagonal(prev, curr):

        if curr[1] + 1 < N and not graph[curr[0]][curr[1] + 1]:
            queue.append([curr, (curr[0], curr[1] + 1)])

        if curr[0] + 1 < N and curr[1] + 1 < N and not graph[curr[0] + 1][curr[1] + 1] and not graph[curr[0]][curr[1] + 1] and not graph[curr[0] + 1][curr[1]]:
            queue.append([curr, (curr[0] + 1, curr[1] + 1)])

        if curr[0] + 1 < N and not graph[curr[0] + 1][curr[1]]:
            queue.append([curr, (curr[0] + 1, curr[1])])

print(cnt)
