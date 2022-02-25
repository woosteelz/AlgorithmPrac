def solution(n):
    answer = 0

    def get_list(n, visited, curr):
        nonlocal answer
        for x in range(len(curr)):
            for y in range(x+1, len(curr)):
                if abs(curr[x] - curr[y]) == abs(x - y):
                    return

        if len(curr) == n:
            answer += 1
            return

        for i in range(n):
            if not visited[i]:
                visited[i] = True
                curr.append(i)
                get_list(n, visited, curr)
                visited[i] = False
                curr.pop()

    get_list(n, [False for _ in range(n)], [])
    return answer
