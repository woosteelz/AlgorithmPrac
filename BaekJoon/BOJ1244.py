# 1244번 스위치 켜고 끄기

def change(a):
    return 0 if a == 1 else 1


def male(num, arr):
    i = num - 1
    while i < len(arr):
        arr[i] = change(arr[i])
        i += num
    return arr


def female(num, arr):
    idx1, idx2 = num-1, num+1
    arr[num] = change(arr[num])
    while idx1 >= 0 and idx2 < len(arr):
        if arr[idx1] == arr[idx2]:
            arr[idx1], arr[idx2] = change(arr[idx1]), change(arr[idx2])
        else:
            break
        idx1 -= 1
        idx2 += 1
    return arr


n = int(input())
switch = list(map(int, input().split()))

m = int(input())
for _ in range(m):
    s, num = map(int, input().split())
    if s == 1:
        switch = male(num, switch)
    else:
        switch = female(num-1, switch)

for i, e in enumerate(switch):
    if i and not (i % 20):
        print()
    print(e, end=' ')
