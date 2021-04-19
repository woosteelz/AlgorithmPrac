# 백준 2156번 포도주 시식
import sys
import math
from collections import deque
from collections import Counter

input = sys.stdin.readline
n = int(input())
wine = []
dp = [0] * n
for _ in range(n):
	wine.append(int(input()))


dp[0] = wine[0]

if n == 1:
	print(wine[0])
elif n == 2:	
	print(sum(wine))
elif n == 3:
	print(max(wine[2] + dp[0], wine[2] + wine[1], wine[0] + wine[1]))
else:
	dp[1] = wine[0] + wine[1]
	dp[2] = max(wine[2] + dp[0], wine[2] + wine[1], wine[0] + wine[1])

	for i in range(3, n):
		dp[i] = max(wine[i] + dp[i-2], wine[i] + wine[i-1] + dp[i-3], wine[i] + wine[i-1] + dp[i-4])
	
	print(max(dp))