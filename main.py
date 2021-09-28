# HackerRank Common Child(Medium)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'commonChild' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

# DP를 이용한 LCS


def commonChild(s1, s2):
    LCS = [[0 for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]
    s1 = ' ' + s1
    s2 = ' ' + s2
    for i in range(1, len(s1)):
        for j in range(1, len(s2)):
            if not s1[j] == s2[i]:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            elif s1[j] == s2[i]:
                LCS[i][j] = LCS[i-1][j-1] + 1

    return max(map(max, LCS))


# print(commonChild('ABCD', 'ABDC'))

def stupid(arr):

    if len(arr) == 2 and arr[0] > arr[1]:
        arr[0], arr[1] = arr[1], arr[0]
        print('#')
    elif len(arr) == 1:
        return
    else:
        m = 2*len(arr) // 3
        stupid(arr[:m-1])
        stupid(arr[len(arr) - m:])
        stupid(arr[:m-1])


visited = [False for _ in range(1000)]
graph = [[] for _ in range(1000)]


def dfs(stack):
    if not stack:
        return
    curr = stack.pop(-1)
    if not graph[curr]:
        print()
    for node in graph[curr]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)
            if len(graph[curr]) == 1:
                print('----', end='')
            elif node == graph[curr][-1]:
                print('L--', end='')
            else:
                print('+--', end='')
            print(my_print(node), end=' ')
            dfs(stack)


def my_print(num):
    temp = str(num)
    return '[' + '0' * (3 - len(temp)) + temp + ']'


for _ in range(5):
    a, b = map(int, input().split())
    graph[a].append(b)

stack = []
stack.append(30)
visited[30] = True
print('[030]--', end=' ')
dfs(stack)
