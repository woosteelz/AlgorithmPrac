# 2628번 종이 자르기

x, y = map(int, input().split())
dir_x = [0, x]
dir_y = [0, y]
for _ in range(int(input())):
    xy, n = map(int, input().split())
    if xy:
        dir_x.append(n)
    else:
        dir_y.append(n)

dir_x.sort()
dir_y.sort()
ans = float('-inf')

for i in range(1, len(dir_x)):
    height = dir_x[i] - dir_x[i-1]
    for j in range(1, len(dir_y)):
        width = dir_y[j] - dir_y[j-1]
        ans = max(ans, height * width)

print(ans)
