# 2477번 참외밭
melon = int(input())
length = []
for _ in range(6):
    a, b = map(int, input().split())
    length.append(b)

idx = length.index(max(length))

if length[idx-1] < length[(idx+1) % 6]:
    idx2 = (idx+1) % 6
else:
    idx2 = idx-1

print((length[idx] * length[idx2] - length[idx-3] * length[idx2-3]) * melon)
