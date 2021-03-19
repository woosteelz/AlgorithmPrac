# 프로그래머스 방문길이 (Level 2)

# 경로가 겹치면 안된다는 것이 핵심 >> 1, 0 -> 0, 1 == 0, 1 -> 1, 0
from collections import deque

def solution(dirs):
	dirs = deque(dirs)
	queue = deque()
	visited = []
	queue.append([0, 0])
	cnt = 0
	while queue and dirs:
		d = dirs.popleft()
		x, y = queue.popleft()
		if d == "U":
			if y+1 <= 5:
				temp_x = x
				temp_y = y + 1
		elif d == "D":
			if y-1 >= -5:
				temp_x = x
				temp_y = y - 1
		elif d == "R":
			if x+1 <= 5:
				temp_x = x + 1
				temp_y = y
		elif d == "L":
			if x-1 >= -5:
				temp_x = x - 1
				temp_y = y 

		if [x, y, temp_x, temp_y] not in visited and [temp_x, temp_y, x, y] not in visited:
			if x == temp_x and y == temp_y:
				pass
			else:
				visited.append([x, y, temp_x, temp_y])
				visited.append([[temp_x, temp_y, x, y]])
				cnt += 1
		queue.append([temp_x, temp_y])
	return cnt

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))
print(solution("LRLRL"))
print(solution("LLLLRLRLRLL"))