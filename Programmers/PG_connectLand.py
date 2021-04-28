# 프로그래머스 섬 연결하기(Level 3)
from collections import deque

def solution(n, costs):
	answer = 0
	costs.sort(key = lambda x:x[2])
	visited = set([costs[0][0]])
	while len(visited) != n:
		for i, cost in enumerate(costs):
			if cost[0] in visited and cost[1] in visited:
				continue
			if cost[0] in visited or cost[1] in visited:
				visited.update([cost[0], cost[1]])
				answer += cost[2]
				costs[i] = [-1, -1, -1]
				break
	return answer
print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))