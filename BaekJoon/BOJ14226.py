# BOJ 14226번 골드바흐의 추측
import sys
from collections import deque

n = int(sys.stdin.readline())
visited = dict()
queue = deque()
queue.append((1, 0))
visited[(1, 0)] = 0

while queue:
	screen, clip = queue.popleft()
	if n == screen:
		print(visited[(screen, clip)])
		break
	
	# 1. 화면의 있는 이모티콘을 모두 복사해서 클립보드에 저장
	if not (screen, screen) in visited.keys():
		visited[(screen, screen)] = visited[(screen, clip)] + 1
		queue.append([screen, screen])
	# 2. 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
	if not (screen + clip, clip) in visited.keys():
		visited[(screen + clip, clip)] = visited[(screen, clip)] + 1
		queue.append((screen + clip, clip))
	# 3. 화면에 있는 이모티콘 중 하나를 삭제
	if not (screen-1, clip) in visited.keys():
		visited[(screen-1, clip)] = visited[(screen, clip)] + 1
		queue.append((screen-1, clip))