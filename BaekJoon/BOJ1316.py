# 백준 1316번 그룹 단어 체커
import sys
import math
from collections import deque
from collections import Counter

def group_word_checker(string):
	curr = string[0]
	check = []
	for i in range(len(string)):
		if curr == string[i]:
			pass
		else:
			if string[i] in check:
				return False
			else:
				check.append(curr)
				curr = string[i]
	return True

n = int(sys.stdin.readline())
ans = 0
for _ in range(n):
	if group_word_checker(sys.stdin.readline()):
		ans += 1

print(ans)