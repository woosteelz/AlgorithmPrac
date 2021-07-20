# SWEA 11387번 몬스터 사냥
TC = int(input())

for tc in range(TC):
    damage = 0
    D, L, N = map(int, input().split())

    for n in range(N):
        damage += (1 + n * L / 100) * D

    print(f'#{tc+1} {int(damage)}')
