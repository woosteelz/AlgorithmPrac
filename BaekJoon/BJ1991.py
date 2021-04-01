# 백준 1991번 트리 순회
import sys

tree = dict()
n = int(sys.stdin.readline())

for _ in range(n):
	a, b, c = map(str, sys.stdin.readline().split())
	tree[a] = [b, c]

pre_ans = []
in_ans = []
post_ans = []

def preorder(node):
	if node == '.':
		return
	else:
		pre_ans.append(node)
		preorder(tree[node][0])
		preorder(tree[node][1])

def inorder(node):
	if node == '.':
		return
	else:
		inorder(tree[node][0])
		in_ans.append(node)
		inorder(tree[node][1])

def postorder(node):
	if node == '.':
		return
	else:
		postorder(tree[node][0])
		postorder(tree[node][1])
		post_ans.append(node)

preorder('A')
inorder('A')
postorder('A')
print(''.join(pre_ans))
print(''.join(in_ans))
print(''.join(post_ans))