# 2635번 수 이어가기
num = int(input())

ans = []

for i in range(num+1):
    temp = [num, i]
    i = 1
    while True:
        if temp[i-1] - temp[i] < 0:
            break
        temp.append(temp[i-1] - temp[i])
        i += 1
    if len(temp) > len(ans):
        ans = temp

print(len(ans))
for i in ans:
    print(i, end=' ')
