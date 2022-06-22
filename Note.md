# Note

### 1. 2차원 배열에서 max()

2차원 배열에서 max()를 사용할 시, 1차원 배열에서 원소의 합이 가장 큰 값의 배열이 나온다.
따라서 각 리스트를 순회하며 찾거나 map을 사용하여 찾는다.

```python
arr = [[1, 2, 3, 4], []5, 6, 7, 8]]
arr_max = max(map(max, arr)) # map을 사용하는 방법
```

min도 마찬가지로 적용하면 된다.

### 2. 2차원 배열의 초기화

2차원 배열에서 초기화를 할 때,

```python
arr = [[0 * n] * n]
```

이런식으로 하면 같은 객체로 인식하기 때문에

```python
arr = [[0 * n] for _ in range(n)]
```

으로 해야한다.

### 3. BFS / DFS 그래프의 인접행렬과 인접리스트 차이

1. BFS(Breadth First Search)
   queue, while을 이용하여 구현.

-   인접리스트

```python
graph = [
	[],
	[], # 1번 노드와 연결된 노드
	[], # 2번 노드와 연결된 노드
	[], # 3번 노드와 연결된 노드
	.
	.
]
```

```python
def BFS(graph, start):
	visited = [False for _ in range(N+1)]
	queue = deque()
	visited[start] = True
	queue.append(start)

	while queue:
		curr = queue.popleft()
		for i in graph[curr]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True
```

-   인접행렬
    N+1 X N+1 인 2중 리스트로 표현(i 와 j 가 연결되어있다면 graph[i][j] = 1 로 표시)

```python
def BFS(graph, start):
	visited = [False for _ in range(N+1)]
	queue = deque()
	visited[start] = True
	queue.append(start)

	while queue:
		curr = queue.popleft()
		for i in range(len(graph[curr])):
			if not visited[i] and graph[curr][i]:
				queue.append(i)
				visited[i] = True
```

BFS는 위 두가지 방식으로 구현 가능하다.
단, 인접행렬의 경우 시간 복잡도가 O(N^2)인 반면
인접리스트의 경우 O(N+E)이다. (E는 간선의 개수)

2. DFS(Depth First Search)
   Stack 또는 Recursion call을 이용

-   인접행렬

```python
def DFS(graph, start):
	visited = [False for _ in range(N+1)]
	stack = list()
	stack.append(start)

	while stack:
		curr = stack[-1]

		for i in range(len(graph[curr])):
			if not visited[i] and graph[curr][i]:
				stack.append(i)
				visited[i] = True
				break
			else:
				stack.pop(-1)
```

-   인접리스트

```python
def DFS(graph, start):
	visited = [False for _ in range(N+1)]
	stack = list()
	stack.append(start)

	while stack:
		curr = stack[-1]

		for i in graph[curr]:
			if not visited[i]:
				stack.append(i)
				visited[i] = True
				break
			else:
				stack.pop(-1)
```

DFS는 두가지 방식으로 구현 가능하다.
단, BFS와 같이 인접행렬로 구현할 때 O(N^2)의 시간 복잡도를,
인접리스트로 구현 할 때 O(N+E)의 시간 복잡도를 가진다.

### 4. input() VS sys.stdin.readline()

```python
import sys
# 입력값 : 알고리즘
a = sys.stdin.readline()
b = input()
```

a에는 알고리즘\n (버퍼가 함께 입력된다.)이,
b에는 알고리즘 이 입력된다.

### 5. 알고리즘 문제 풀이시

프로그래머스 점프와 순간이동을 풀면서.  
처음 문제를 봤을때 BFS를 이용한 풀이라고 생각하고 다른 방법은 생각하지도 않았다.

그러나 BFS를 사용해 문제를 풀었을때 정답은 맞았지만 시간초과가 떠서 다른 방법을 찾았다.

그냥 단순히 2로 나누어 나머지가 1일 경우에만 Count하면 된다....

-   수학문제가 아니다. 충분히 생각하고 코드를 작성하는 습관을 들이자.

### 6. LCS(Longest Common Substring) vs LCS(Longest Common Subsequence)

#### 1. Longest Common Substring

연속된 공통 문자열을 뜻한다.  
ex) ABCDEF, GBCDFE => BCD

1. 점화식

    1. 문자열 A와 B를 한글자씩 비교한다.
    2. 두 문자가 다르면 LCS[i][j]에 0을 저장한다.
    3. 두 문자가 같다면 LCS[i-1][j-1] 값에 1을 더해 저장한다.
    4. 위 과정을 반복한다.

```python
if i == 0 or j == 0: # DP를 위한 마진값 설정
	LCS[i][j] = 0
elif s1[i] == s2[j]: # 두 문자열이 같다면
	LCS[i][j] = LCS[i-1][j-1] + 1
else: # 두 문자열이 다르다면
	LCS[i][j] = 0
```

2. CODE

```python
def LongestCommonSubstring(s1, s2):
	m, n = len(s2), len(s1)
	LCS = [[0 for _ in range(m+1)] for _ in range(n+1)] # 2차원 배열 초기화
	s1, s2 = ' ' + s1, ' ' + s2 # 마진값

	for i i n range(1, n+1):
		for j in range(1, m+1):
			if not s1[j] == s2[i]:
				LCS[i][j] = 0
			else:
				LCS[i][j] = LCS[i-1][j-1] + 1

	return max(map(max, LCS))
```

#### 2. Longest Common Subsequence

연속되지 않아도 공통인 최장길이 문자열  
ex) ABCDEF, GBCDFE => BCDE or BCDF

1. 점화식

    1. 문자열 A와 B를 한글자씩 비교한다.
    2. 두 문자가 다르면 LCS[i][j]에 max(LCS[i-1][j], LCS[i][j-1])을 저장
    3. 두 문자가 같다면 LCS[i-1][j-1] 값에 1을 더해 저장한다.
    4. 위 과정을 반복한다.

```python
if i == 0 or j == 0: # DP를 위한 마진값 설정
	LCS[i][j] = 0
elif s1[i] == s2[j]: # 두 문자열이 같다면
	LCS[i][j] = LCS[i-1][j-1] + 1
else: # 두 문자열이 다르다면
	LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
```

2. CODE

```python
def LongestCommonSubsequence(s1, s2):
	m, n = len(s2), len(s1)
	LCS = [[0 for _ in range(m+1)] for _ in range(n+1)] # 2차원 배열 초기화
	s1, s2 = ' ' + s1, ' ' + s2 # 마진값

	for i in range(1, n+1):
		for j in range(1, m+1):
			if not s1[j] == s2[i]:
				LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
			else:
				LCS[i][j] = LCS[i-1][j-1] + 1

	return max(map(max, LCS))
```

2-1. 문자열 추출

```python
i, j = n, m
    ans = ''
    while i > 0 and j > 0:
        if LCS[i][j-1] == LCS[i][j]:
            j -= 1
        elif LCS[i-1][j] == LCS[i][j]:
            i -= 1
        else:
            ans = s1[j] + ans
            i -= 1
            j -= 1
	print(ans)
```
