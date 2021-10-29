# 20057번 마법사 상어와 토네이도
left = [[-2, 0, 2], [-1, -1, 10], [-1, 0, 7], [-1, 1, 1],
        [0, -2, 5], [1, -1, 10], [1, 0, 7], [1, 1, 1], [2, 0, 2]]
right = [[-2, 0, 2], [-1, -1, 1], [-1, 0, 7], [-1, 1, 10],
         [0, 2, 5], [1, -1, 1], [1, 0, 7], [1, 1, 10], [2, 0, 2]]
top = [[-2, 0, 5], [-1, -1, 10], [-1, 1, 10], [0, -2, 2],
       [0, 2, 2], [0, -1, 7], [0, 1, 7], [1, -1, 1], [1, 1, 1]]
down = [[2, 0, 5], [-1, -1, 1], [-1, 1, 1], [0, -2, 2],
        [0, 2, 2], [0, -1, 7], [0, 1, 7], [1, -1, 10], [1, 1, 10]]


def move_left(x, y):
    temp = 0
    out = 0
    for i, j, val in left:
        temp += graph[x][y] * val // 100
        if 0 <= x + i < N and 0 <= y + j < N:
            graph[x+i][y+j] += graph[x][y] * val // 100
        else:
            out += graph[x][y] * val // 100

    if y-1 >= 0:
        graph[x][y-1] += graph[x][y] - temp
    else:
        out += graph[x][y] - temp
    return out


def move_right(x, y):
    temp = 0
    out = 0
    for i, j, val in right:
        temp += graph[x][y] * val // 100
        if 0 <= x + i < N and 0 <= y + j < N:
            graph[x+i][y+j] += graph[x][y] * val // 100
        else:
            out += graph[x][y] // 100

    if y+1 < N:
        graph[x][y+1] += graph[x][y] - temp
    else:
        out += graph[x][y] - temp
    return out


def move_top(x, y):
    temp = 0
    out = 0
    for i, j, val in top:
        temp += graph[x][y] * val // 100
        if 0 <= x + i < N and 0 <= y + j < N:
            graph[x+i][y+j] += graph[x][y] * val // 100
        else:
            out += graph[x][y] * val // 100

    if x-1 >= 0:
        graph[x-1][y] += graph[x][y] - temp
    else:
        out += graph[x][y] - temp
    return out


def move_down(x, y):
    temp = 0
    out = 0
    for i, j, val in down:
        temp += graph[x][y] * val // 100
        if 0 <= x + i < N and 0 <= y + j < N:
            graph[x+i][y+j] += graph[x][y] * val // 100
        else:
            out += graph[x][y] * val // 100

    if x+1 < N:
        graph[x+1][y] += graph[x][y] - temp
    else:
        out += graph[x][y] - temp
    return out


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

curr_x, curr_y = N // 2, N // 2
ans = 0
move = 0
to_go = 1
dir = 0
flag = False
while True:
    for _ in range(to_go):
        if dir == 0:
            curr_y -= 1
            ans += move_left(curr_x, curr_y)
        elif dir == 1:
            curr_x += 1
            ans += move_down(curr_x, curr_y)
        elif dir == 2:
            curr_y += 1
            ans += move_right(curr_x, curr_y)
        elif dir == 3:
            curr_x -= 1
            ans += move_top(curr_x, curr_y)
        graph[curr_x][curr_y] = 0

        if curr_x == 0 and curr_y == 0:
            flag = True
            break
    dir = (dir + 1) % 4
    move += 1
    if move == 2:
        move = 0
        to_go += 1
    if flag:
        break

print(ans)
