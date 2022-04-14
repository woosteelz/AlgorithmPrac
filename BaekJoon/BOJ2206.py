# BOJ 2206번 벽 부수고 이동하기
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = []

for _ in range(n):
	graph.append(list(map(int, list(input().strip()))))

visited = [[[0 for _ in range(2)] for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append([0, 0, 0])
visited[0][0][0] = 1

dir_x = [0, 0, 1, -1]
dir_y = [1, -1, 0, 0]
flag = True
def bfs():
    while queue:
        curr_x, curr_y, cnt = queue.popleft()
        if curr_x == n-1 and curr_y == m-1:
           return visited[curr_x][curr_y][cnt]

        for i in range(4):
            next_x, next_y = curr_x + dir_x[i], curr_y + dir_y[i]
            if 0 <= next_x < n and 0 <= next_y < m:
                if graph[next_x][next_y] == 1 and cnt == 0:
                    queue.append([next_x, next_y, 1])
                    visited[next_x][next_y][1] = visited[curr_x][curr_y][0] + 1
                if graph[next_x][next_y] == 0 and visited[next_x][next_y][cnt] == 0:
                    queue.append([next_x, next_y, cnt])
                    visited[next_x][next_y][cnt] = visited[curr_x][curr_y][cnt] + 1
    return -1

print(bfs())
