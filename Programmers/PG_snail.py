def solution(n):
    answer = []
    graph = [[0 for _ in range(n)] for _ in range(n)]

    curr_x = 0
    curr_y = -1

    num = 1

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                curr_y += 1
            elif i % 3 == 1:
                curr_x += 1
            elif i % 3 == 2:
                curr_x -= 1
                curr_y -= 1
            graph[curr_y][curr_x] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if not graph[i][j]:
                answer.append(graph[i][j])

    return answer
