# 백준 문제번호 11399번 ATM

import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
  start, end = map(int, sys.stdin.readline().split())
  arr.append((start, end))

arr.sort(key=lambda x:(x[1], x[0]))
print(arr)

ans = 0
prev = 0
for a in arr:
  if a[0] >= prev:
    prev = a[1]
    ans += 1
print(ans)