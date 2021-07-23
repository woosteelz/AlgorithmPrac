# 2116번 주사위 쌓기

n = int(input())
top_bottom = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0}
ans = []

first_dice = list(map(int, input().split()))
dices = [list(map(int, input().split())) for _ in range(n-1)]

bottom = 0
top = 0

for idx in range(6):
    bottom = first_dice[idx]
    top = first_dice[top_bottom[idx]]
    temp = max([x for x in first_dice if x not in [top, bottom]])

    for dice in dices:
        temp_idx = dice.index(top)
        bottom = dice[temp_idx]
        top = dice[top_bottom[temp_idx]]
        temp += max([x for x in dice if x not in [bottom, top]])
    ans.append(temp)
print(max(ans))
