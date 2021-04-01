# 프로그래머스 캐시(Level 2)
from collections import deque

def solution(cacheSize, cities):
	answer = 0
	cache = deque(maxlen=cacheSize)
	while cities:
		temp = cities.pop(0).lower()
		if temp in cache:
			cache.remove(temp)
			cache.append(temp)
			answer += 1
		else:
			cache.append(temp)
			answer += 5
	return answer

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))