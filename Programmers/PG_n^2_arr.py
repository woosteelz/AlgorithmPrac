import pprint


def solution(n, left, right):
    arr = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            curr = i if i > j else j
            arr[i][j] = curr + 1

    temp = []
    for i in range(n):
        temp += arr[i]

    return temp[left:right]
