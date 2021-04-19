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

+ 인접리스트
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

+ 인접행렬
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

+ 인접행렬
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

+ 인접리스트
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
a에는 알고리즘\n 이(버퍼가 함께 입력된다.)
b에는 알고리즘 이 입력된다.