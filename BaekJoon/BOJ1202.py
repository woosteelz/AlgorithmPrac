# 1202번 보석 도둑
import sys

N, K = map(int, sys.stdin.readline().split())
jewel = []
bags = []
for _ in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewel.append((M, V))
for _ in range(K):
    bags.append(int(sys.stdin.readline()))

jewel.sort(key=lambda x: (x[1], x[0]), reverse=True)
bags.sort()
value = 0

while bags:
    if jewel[0][0] <= bags[-1]:
        value += jewel[0][1]
        jewel.pop(0)
        bags.pop(0)


print(value)
