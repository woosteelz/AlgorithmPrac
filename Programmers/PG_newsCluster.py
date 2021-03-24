# 프로그래머스 뉴스 클러스터링 (Level 2)
import itertools
import math

def solution(str1, str2):
	answer = 0
	str1 = str1.upper()
	str2 = str2.upper()
	a = []
	b = []
	for i in range(1, len(str1)):
		temp = ''
		if str1[i].isalpha() and str1[i-1].isalpha():
			temp += str1[i-1] + str1[i]
		if temp:
			a.append(temp)
	for i in range(1, len(str2)):
		temp = ''
		if str2[i].isalpha() and str2[i-1].isalpha():
			temp += str2[i-1] + str2[i]
		if temp:
			b.append(temp)

	common = []
	for i in a:
		if i in b:
			common.append(i)
			b.remove(i)
	
	sum_arr = len(a) + len(b)

	if sum_arr:
		return math.trunc(len(common)/sum_arr*65536)
	else:
		return 65536


print(solution('FRANCE', 'french'))
print(solution('E=M*C^2', 'e=m*c^2'))
print(solution('aa1+aa2','AAAA12'))
print(solution('handshake','shake hands'))