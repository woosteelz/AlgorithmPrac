# 프로그래머스 전력망을 둘로 나누기
from collections import deque


def solution(n, wires):
    answer = []

    def bfs(node, x, y):
        queue = deque()
        queue.append(node)
        visited[node] = True
        while queue:
            curr = queue.popleft()
            for next_node in graph[curr]:
                if not visited[next_node] and not sorted([curr, next_node]) == sorted([x, y]):
                    queue.append(next_node)
                    visited[next_node] = True

    graph = [[] for _ in range(n+1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [False for _ in range(n+1)]
        for i in range(1, n+1):
            if not visited[i]:
                bfs(i, a, b)
                break
        answer.append(abs(sum(visited) - (n-sum(visited))))

    return min(answer)


print(solution(4, [[1, 2], [2, 3], [3, 4]]))
print(solution(9, [[1, 3], [2, 3], [3, 4], [
      4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
