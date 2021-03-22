# 프로그래머스 오픈채팅방 (Level 2)

def solution(record):
	answer = []
	ans = []
	name = dict()
	for i in range(len(record)):
		temp = list(record[i].split())
		if temp[0] == 'Enter':
			answer.append([temp[1], '님이 들어왔습니다.'])
			name[temp[1]] = temp[2]
		elif temp[0] == 'Leave':
			answer.append([temp[1], '님이 나갔습니다.'])
		elif temp[0] == 'Change':
			name[temp[1]] = temp[2]

	for i in range(len(answer)):
		ans.append(name[answer[i][0]] + answer[i][1])
	
	return ans

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))