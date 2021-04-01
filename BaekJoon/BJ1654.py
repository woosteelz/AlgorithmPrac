# 백준 1654번 랜선 자르기
import sys

k, n = map(int, sys.stdin.readline().split())
lan_line = list()

for _ in range(k):
	lan_line.append(int(sys.stdin.readline()))

left = 1
right = max(lan_line)
mid = (left + right) // 2
while left <= right:
	mid = (left + right) // 2
	temp = 0
	for i in lan_line:
		temp += i // mid
	if temp < n:
		right = mid - 1
	else:
		left = mid + 1
print(right)

