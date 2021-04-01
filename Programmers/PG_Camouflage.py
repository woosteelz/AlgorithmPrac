# 프로그래머스 위장 (Level 2)

def solution(clothes):
	new_clothes = dict()
	for cloth, category in clothes:
		if category in new_clothes:
			new_clothes[category] += 1
		else:
			new_clothes[category] = 1

	temp = []
	
	for category in new_clothes:
		temp.append(new_clothes[category]+1)
	ans = 1
	for t in temp:
		ans *= t

	return ans-1

print(solution([["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]]))