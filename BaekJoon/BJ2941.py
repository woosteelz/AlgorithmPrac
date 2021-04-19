# 백준 2941번 크로아티아 알파벳
import sys
import math
from collections import deque
from collections import Counter

crotic_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = sys.stdin.readline()
ans = 0
i = 0
while i < len(word):
	if i + 2 < len(word):
		temp = word[i] + word[i+1] + word[i+2]
		if temp in crotic_alpha:
			ans += 1
			i += 3
		else:
			temp = word[i] + word[i+1]
			if temp in crotic_alpha:
				ans += 1
				i += 2
			else:
				i += 1
				ans += 1
	elif i + 1 < len(word):
		temp = word[i] + word[i+1]
		if temp in crotic_alpha:
			ans += 1
			i += 2
		else:
			i += 1
			ans += 1
	else:
		i += 1
		ans += 1


print(ans-1)
	