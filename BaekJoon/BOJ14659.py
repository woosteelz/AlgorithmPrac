# 백준 문제번호 14659번 한조서열정리하고옴ㅋㅋ

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
ans = 0
cnt = 0
maxHeight = 0
for i in range(N):
  if arr[i] > maxHeight:
    cnt = 0
    maxHeight = arr[i]
  else:
    cnt += 1
  ans = max(ans, cnt)
print(ans)
