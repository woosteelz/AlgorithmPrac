import sys
import math
from collections import deque
from collections import Counter

input = sys.stdin.readline
n = int(input())
triangle = []
for _ in range(n):
	triangle.append(list(map(int, input().split())))
triangle = triangle[::-1]

for i in range(1, n):
	for j in range(len(triangle[i])):
		if triangle[i-1][j] > triangle[i-1][j+1]:
			triangle[i][j] += triangle[i-1][j]
		else:
			triangle[i][j] += triangle[i-1][j+1]
print(triangle[n-1][0])