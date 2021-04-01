# 백준 1436번 영화감독 숌
import sys

n = int(sys.stdin.readline())
cnt = 0
world_end = 666
while True:
    if '666' in str(world_end):
        cnt += 1
    if cnt == n:
        print(world_end)
        break
    world_end += 1