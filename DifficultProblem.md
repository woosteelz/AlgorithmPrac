# 어려웠던 문제 모음

### 1. 프로그래머스 - N으로 표현 (Dynamic Programming)
1. 문제
아래와 같이 5와 사칙연산만으로 12를 표현할 수 있습니다.
12 = 5 + 5 + (5 / 5) + (5 / 5)
12 = 55 / 5 + 5 / 5
12 = (55 + 5) / 5
5를 사용한 횟수는 각각 6,5,4 입니다. 그리고 이중 가장 작은 경우는 4입니다.
이처럼 숫자 N과 number가 주어질 때, N과 사칙연산만 사용해서 표현 할 수 있는 방법 중 N 사용횟수의 최솟값을 return 하도록 solution 함수를 작성하세요.
2. 제한사항
- N은 1 이상 9 이하입니다.
- number는 1 이상 32,000 이하입니다.
- 수식에는 괄호와 사칙연산만 가능하며 나누기 연산에서 나머지는 무시합니다.
- 최솟값이 8보다 크면 -1을 return 합니다.
3. 입출력 예
N = 5, number = 12 > answer = 4
N = 2, number = 11 > answer = 3
4. 풀이 
ex) N = 3,
> N을 1회 사용: 3 
N을 2회 사용: 33, 3+3=6, 3-3=0,3*3=9, 3/3=1
N을 3회 사용: 333, 3+3+3=9, ...

 규칙: 
 > N이 2개일 경우: 1개인 경우의 수 (+, -, /, *) 1개인 경우의 수
 N이 3개일 경우: 1개인 경우의 수 (+, -, /, *) 2개인 경우의 수 + 1개인 경우의 수 (+, -, /, *) 2개인 경우의 수
				.
				.
				.
 N이 N개일 경우: 1개인 경우의 수 (+, -, /, *) N-1개인 경우의 수 + ... + N-1개인 경우의 수 (+, -, /, *) 1개인 경우의 수

 * 사칙연산에서 곱셈과 덧셈은 결과에 차이가 없지만 나머지는 차이가 있기 때문에 순서를 바꿔서 연산을 한번 더 수행한다.


### 2. 프로그래머스 - 가장 큰 정사각형 찾기 (Level 2)

1. 문제
1와 0로 채워진 표(board)가 있습니다. 표 1칸은 1 x 1 의 정사각형으로 이루어져 있습니다. 표에서 1로 이루어진 가장 큰 정사각형을 찾아 넓이를 return 하는 solution 함수를 완성해 주세요. (단, 정사각형이란 축에 평행한 정사각형을 말합니다.)
예를 들어
> 1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0

 가 있다면 가장 큰 정사각형은
> 1	2	3	4
0	1	1	1
1	1	1	1
1	1	1	1
0	0	1	0

 가 되며 넓이는 9가 되므로 9를 반환해 주면 됩니다.

2. 제한사항
+ 표(board)는 2차원 배열로 주어집니다.
+ 표(board)의 행(row)의 크기 : 1,000 이하의 자연수
+ 표(board)의 열(column)의 크기 : 1,000 이하의 자연수
+ 표(board)의 값은 1또는 0으로만 이루어져 있습니다.

3. 내 풀이
board의 각 원소를 순회하며 DFS 실시... (시간 초과)
```python
from collections import deque
import math

def check(visited, board, a, b, N, M):
	queue = deque()
	dir_x = [1, 0, 1]
	dir_y = [0, 1, 1]
	queue.append([a, b])
	visited[a][b] = True
	temp = [[0 for _ in range(M)] for _ in range(N)]
	while queue:
		x, y = queue.popleft()
		for i in range(3):
			temp_x = x + dir_x[i]
			temp_y = y + dir_y[i]
			if 0<= temp_x < N and 0 <= temp_y < M and board[temp_x][temp_y] and not visited[temp_x][temp_y]:
				visited[temp_x][temp_y] = True
				temp[temp_x][temp_y] = 1 + temp[x][y]
				queue.append([temp_x, temp_y])
	
	if N < M:
		answer = [0] * M
	else:
		answer = [0] * N
	for i in range(N):
		for j in range(M):
			answer[temp[i][j]] += 1
	for i in range(len(answer)-1, 0, -1):
		if answer[i] == i*2+1:
			return i+1
	return 0

def solution(board):
	N = len(board)
	M = len(board[0])
	ans = []
	for i in range(N):
		for j in range(M):
			visited = [[False for _ in range(M)] for _ in range(N)]
			if board[i][j]:
				ans.append(check(visited, board, i, j, N, M))
	return max(ans) ** 2
```
4. 다른 사람의 풀이
Dynamic Programming 이용

```python
def solution(board):
	N = len(board)
	M = len(board[0])
	for i in range(1, N):
		for j in range(1, M):
			if board[i][j]:
				board[i][j] += min(board[i-1][j-1], board[i][j-1], board[i-1][j])
	ans = max(board[0])
	for i in range(1, N):
		if ans < max(board[i]):
			ans = max(board[i])
	return ans ** 2
```
