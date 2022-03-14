n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def up(board): # 위
    for i in range(n): 
        curr = 0 # 현재 이동
        val = 0 # 넣을 값
        for j in range(n):
            if board[j][i] == 0:
                continue 
            if val == 0:
                val = board[j][i]
            else:
                if val == board[j][i]: # 이동한 곳이 이전값과 같을 경우
                    board[curr][i] = val * 2 
                    val = 0
                    curr += 1 
                else: # 다를 경우
                    board[curr][i] = val
                    val = board[j][i]
                    curr += 1
            board[j][i] = 0
        if val:
            board[curr][i] = val 
    return board


def down(board):
    for i in range(n): 
        curr = n - 1
        val = 0
        for j in range(n - 1, -1, -1): 
            if board[j][i] == 0: continue 
            if val == 0:
                val = board[j][i]
            else:
                if val == board[j][i]:
                    board[curr][i] = val * 2 
                    val = 0 
                    curr -= 1
                else:
                    board[curr][i] = val
                    val = board[j][i]
                    curr -= 1
            board[j][i] = 0
        if val:
            board[curr][i] = val
    return board


def right(board):
    for i in range(n):
        curr = n - 1
        val = 0
        for j in range(n - 1, -1, -1): 
            if board[i][j] == 0: continue
            if val == 0: val = board[i][j]
            else:
                if val == board[i][j]:
                    board[i][curr] = val * 2 
                    val = 0
                    curr -= 1
                else:
                    board[i][curr] = val
                    val = board[i][j]
                    curr -= 1 
            board[i][j] = 0 
        if val:
            board[i][curr] = val
    return board


def left(board):
    for i in range(n):
        curr = 0
        val = 0
        for j in range(n):
            if board[i][j] == 0: 
                continue 
            if val == 0: 
                val = board[i][j]
            else:
                if val == board[i][j]:
                    board[i][curr] = val * 2
                    val = 0
                    curr += 1
                else:
                    board[i][curr] = val
                    val = board[i][j]
                    curr += 1
            board[i][j] = 0
        if val:
            board[i][curr] = val
    return board

def my_copy(arr):
    temp = []
    for i in range(len(arr)):
        temp.append(arr[i][:])
    return temp


def solution(board, cnt):
    global ans
    if cnt == 5:
        ans = max(ans, max(map(max, board)))
        return

    solution(left(my_copy(board)), cnt + 1)
    solution(right(my_copy(board)), cnt + 1)
    solution(up(my_copy(board)), cnt + 1)
    solution(down(my_copy(board)), cnt + 1)

ans = 0
solution(arr, 0)
print(ans)