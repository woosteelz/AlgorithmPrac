# 백준 문제번호 1202번 보석 도둑

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

while jewel:
    temp = jewel.pop(0)
    if sum(bags):
        for i in range(len(bags)):
            if bags[i] >= temp[0]:
                value += temp[1]
                bags[i] = 0
                break
    bags.sort()

print(value)
