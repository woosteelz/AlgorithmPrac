# BOJ 14500번 테트로미노
import sys

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# oooo
def check1(x, y):
	if y + 3 < m:
		return graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x][y+3]
	else:
		return 0
def check2(x, y):
	if x + 3 < n:
		return graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+3][y]
	else:
		return 0

# oo
# oo
def check3(x, y):
	if x + 1 < n and y + 1 < m:
		return graph[x][y] + graph[x+1][y] + graph[x][y+1] + graph[x+1][y+1]
	else:
		return 0

# o
# o
# oo
def check4(x, y):
	if x + 2 < n and y + 1 < m:
		return max(
			graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+2][y+1],
			graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+2][y+1], 
			graph[x][y+1] + graph[x+1][y+1] + graph[x+2][y+1] + graph[x+2][y], 
			graph[x][y] + graph[x][y+1] + graph[x+1][y] + graph[x+2][y]
		)
	else:
		return 0
def check5(x, y):
	if x + 1 < n and y + 2 < m:
		return max(
			graph[x+1][y] + graph[x+1][y+1] + graph[x+1][y+2] + graph[x][y+2], 
			graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y], 
			graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+1][y+2], 
			graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+2]
		)
	else:
		return 0

# o
# oo
#  o
def check6(x, y):
	if x + 2 < n and y + 1 < m:
		return max(
			graph[x][y] + graph[x+1][y] + graph[x+1][y+1] + graph[x+2][y+1], 
			graph[x][y+1] + graph[x+1][y+1] + graph[x+1][y] + graph[x+2][y]
		)
	else:
		return 0
def check7(x, y):
	if x + 1 < n and y + 2 < m:
		return max(
			graph[x][y+1] + graph[x][y+2] + graph[x+1][y] + graph[x+1][y+1], 
			graph[x][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+1][y+2]
		)
	else:
		return 0

# ooo
#  o
def check8(x, y):
	if x + 1 < n and y + 2 < m:
		return max(
			graph[x][y] + graph[x][y+1] + graph[x][y+2] + graph[x+1][y+1], 
			graph[x+1][y] + graph[x+1][y+1] + graph[x+1][y+2] + graph[x][y+1]
		)
	else:
		return 0 
def check9(x, y):
	if x + 2 < n and y + 1 < m:
		return max(
			graph[x][y] + graph[x+1][y] + graph[x+2][y] + graph[x+1][y+1], 
			graph[x+1][y] + graph[x][y+1] + graph[x+1][y+1] + graph[x+2][y+1]
		)
	else:
		return 0

ans = []
for i in range(n):
	for j in range(m):
		ans.append(check1(i, j))
		ans.append(check2(i, j))
		ans.append(check3(i, j))
		ans.append(check4(i, j))
		ans.append(check5(i, j))
		ans.append(check6(i, j))
		ans.append(check7(i, j))
		ans.append(check8(i, j))
		ans.append(check9(i, j))
print(max(ans))
