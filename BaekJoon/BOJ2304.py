# 2304번 창고 다각형

N = int(input())
pillars = [list(map(int, input().split())) for _ in range(N)]
pillars.sort()
pos = []
height = []
pillar_dict = {}

for a, b in pillars:
    pos.append(a)
    height.append(b)
    pillar_dict[a] = b

idx = pos[height.index(max(height))]
area = 0
high = 0

for i in range(0, idx+1):
    if i in pillar_dict and high < pillar_dict[i]:
        high = pillar_dict[i]
    area += high
high = 0
for i in range(pos[-1], idx, -1):
    if i in pillar_dict and high < pillar_dict[i]:
        high = pillar_dict[i]
    area += high
print(area)
