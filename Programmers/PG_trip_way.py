from collections import deque


def solution(tickets):
    answer = deque()
    routes = dict()

    for depart, destiny in tickets:
        if depart in routes:
            routes[depart].append(destiny)
        else:
            routes[depart] = [destiny]
    for k in routes:
        routes[k].sort(reverse=True)

    stack = deque(['ICN'])
    while stack:
        curr = stack[-1]
        if curr in routes and routes[curr]:
            stack.append(routes[curr].pop())
        else:
            answer.append(stack.pop())

    return list(answer)[::-1]
