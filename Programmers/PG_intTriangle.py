# 프로그래머스 정수 삼각형 (Level 3)

def solution(triangle):
	triangle = triangle[::-1]
	for i in range(1, len(triangle)):
		for j in range(len(triangle[i])):
			if triangle[i-1][j] >= triangle[i-1][j+1]:
				triangle[i][j] += triangle[i-1][j]
			else:
				triangle[i][j] += triangle[i-1][j+1]
			print(triangle)
	return triangle[len(triangle)-1][0]


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))