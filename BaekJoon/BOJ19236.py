from copy import deepcopy
from pprint import pprint
graph = []
for _ in range(4):
    temp = []
    arr = list(map(int, input().split()))
    for i in range(4):
        temp.append([arr[2 * i], arr[2 * i + 1] - 1])
    graph.append(temp)

way = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]

def get_fish(a, num):
    for i in range(4):
        for j in range(4):
            if a[i][j][0] == num:
                return [i, j]
    return False

def get_eat(x, y, eat, arr):
    global ans

    # 물고기 먹고
    eat += arr[x][y][0]
    arr[x][y][0] = 0

    # 1 ~ 16까지 확인후 이동
    for i in range(16):
        curr = get_fish(arr, i+1)
        if not curr:
            continue

        for d in range(8):
            curr_dir = (arr[curr[0]][curr[1]][1] + d) % 8
            # print(curr_dir)
            next_x, next_y = curr[0] + way[curr_dir][0], curr[1] + way[curr_dir][1]

            if 0 <= next_x < 4 and 0 <= next_y < 4 and not [next_x, next_y] == [x, y]:
                arr[curr[0]][curr[1]][1] = curr_dir
                arr[curr[0]][curr[1]], arr[next_x][next_y] = arr[next_x][next_y], arr[curr[0]][curr[1]]
                break
    

    for i in range(1, 4):
        next_x, next_y = x + way[arr[x][y][1]][0] * i, y + way[arr[x][y][1]][1] * i
        if 0 <= next_x < 4 and 0 <= next_y < 4 and arr[next_x][next_y][0] > 0:
            get_eat(next_x, next_y, eat, deepcopy(arr))

    ans = max(ans, eat)
ans = 0
get_eat(0, 0, 0, graph)
print(ans)