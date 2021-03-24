# 프로그래머스 압축(Level 2)
from collections import deque

def solution(files):
	answer = []
	temp = 'abcdefghijklmnopqrstuvwxyz'
	temp = temp.upper()
	new_dict = dict()
	files = list(files)

	for i in range(26):
		new_dict[temp[i]] = i+1

	i = 27
	temp = ''
	while files:
		temp += files.pop(0)
		if temp not in new_dict:
			answer.append(new_dict[temp[:len(temp)-1]])
			new_dict[temp] = i
			i += 1
			files.insert(0, temp[-1])
			temp = ''
	answer.append(new_dict[temp])
	return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))