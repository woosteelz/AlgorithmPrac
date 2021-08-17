# 1208번 부분수열의 합

num, total = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
# for i in range(1 << num):
#     temp = 0
#     for j in range(num):
#         if i & (1 << j):
#             temp += arr[j]
#     if temp == total:
#         ans += 1

# print(ans) if total else print(ans-1)

'''
left = arr[:num//2]
right = arr[num//2:]
left_ans = []
right_ans = []

for i in range(1 << len(left)):
    temp = 0
    for j in range(len(left)):
        if i & (1 << j):
            temp += left[j]
    left_ans.append(temp)

for i in range(1 << len(right)):
    temp = 0
    for j in range(len(right)):
        if i & (1 << j):
            temp += right[j]
    right_ans.append(temp)

print(left_ans, right_ans)

ans = 0
for l in left_ans:
    for r in right_ans:
        if l + r == total:
            ans += 1

print(ans - 1)
'''
# 시간초과

# 아이디어
'''
배열을 나누어 이분탐색
1. 배열을 절반으로 나눔
2. 각각의 배열의 부분수열의 합을 구해 정렬
3. 왼쪽 배열의 0번 인덱스, 오른쪽 배열의 마지막 인덱스에서 접근하여 total값과 비교하며 start, end값을 변경

-1, 0, 1, 2, 3, 4 target = 1
left -1 -1 0 0 0 0 1 1 
right 0 2 3 4 5 6 7 9
target = 0
ans - 1

DFS(stack) / BFS(queue)
하는중..
'''
