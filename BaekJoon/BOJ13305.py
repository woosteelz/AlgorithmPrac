# 백준 문제번호 13305번 주유소

import sys

N = int(sys.stdin.readline())
road = list(map(int, sys.stdin.readline().split()))
station = list(map(int, sys.stdin.readline().split()))

cost = 0
sum_road = 0
min_price = station[0]
for i in range(N-1):
  if station[i] < min_price:
    cost += min_price * sum_road
    min_price = station[i]
    sum_road = 0
  sum_road += road[i]
if sum_road:
  cost += min_price * sum_road

print(cost)