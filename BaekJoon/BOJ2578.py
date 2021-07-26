# 2578번 빙고
bingo = [list(map(int, input().split())) for _ in range(5)]
judge = []
for _ in range(5):
    judge += list(map(int, input().split()))

visited = [[0 for _ in range(5)] for _ in range(5)]
row = [0] * 5
col = [0] * 5
cross = [0, 0]


def isbingo(arr, row, col, cross):
    # 가로
    for i in range(5):
        if sum(arr[i]) == 5:
            col[i] = 1
    # 세로
    for i in range(5):
        temp = 0
        for j in range(5):
            temp += arr[j][i]
        if temp == 5:
            row[i] = 1
    # 대각선
    left = 0
    right = 0
    for i in range(5):
        left += arr[i][i]
        right += arr[4-i][i]
    if left == 5:
        cross[0] = 1
    if right == 5:
        cross[1] = 1

    return row, col, cross


cnt = 0
for num in judge:
    cnt += 1
    for i in range(5):
        if num in bingo[i]:
            visited[i][bingo[i].index(num)] = 1
            break
    if cnt >= 5:
        row, col, cross = isbingo(visited, row, col, cross)
        if sum(row) + sum(col) + sum(cross) >= 3:
            print(cnt)
            break
