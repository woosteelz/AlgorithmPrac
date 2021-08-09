# 1120번 문자열

A, B = input().split()

ans = []

for i in range(len(B) - len(A) + 1):
    cnt = 0
    j = 0
    while j < len(A):
        if not A[j] == B[j + i]:
            cnt += 1
        j += 1
    ans.append(cnt)
print(min(ans))
