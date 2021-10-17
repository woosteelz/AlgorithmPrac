# 프로그래머스 전력망을 둘로 나누기

def solution(n, wires):
    answer = -1

    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for a, b in wires:
        graph[a][b] = 1
        graph[b][a] = 1

    for a, b in wires:
        graph[a][b] = 0
        graph[b][a] = 0

        # BFS 돌리기

        graph[a][b] = 1
        graph[b][a] = 1

    return answer
