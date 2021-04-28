# 프로그래머스 점프와 순간 이동 (Level 2)
from collections import deque

def solution(n):
	visited = [0] * (n+1)
	queue = deque()
	queue.append(0)
	visited[0] = 1
	while queue:
		curr = queue.popleft()
		print(visited)
		if visited[n]:
			return visited[n]-1
		# 순간이동 하는 경우 비용이 가장 적게 들기 때문에 큐의 맨 앞에 삽입
		if curr * 2 <= n and not visited[curr*2]:
			visited[curr*2] = visited[curr]
			queue.appendleft(curr*2)
		# 점프하는 경우
		if curr+1 <= n and not visited[curr+1]:
			visited[curr+1] = visited[curr] + 1
			queue.append(curr+1)
print(solution(6))

# 다른 사람의 풀이
def solution(n):
	return bin(n).count('1')

# ㅋㅋ최단거리라고 해서 무조건 BFS인줄 알았건만 더 간단한 방법이 있다.
# 무작정 알고리즘부터 들이밀 생각하지 말고 일차원적으로 생각해볼 필요성이 있다.