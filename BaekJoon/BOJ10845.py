# 백준 문제번호 10845번 큐

# 1. deque가 list보다 빠름
# 2. input()의 속도가 sys.stdin.readline()보다 느림
# 3. 이 문제에서 deque를 사용하나 list를 사용하나 차이는 없음. 2번의 문제

from collections import deque
import sys

def q_push(Q, num):
  Q.append(num)

def q_pop(Q):
  if Q:
    print(Q.popleft())
  else:
    print("-1")

def q_front(Q):
  if Q:
    print(Q[0])
  else:
    print("-1")

def q_back(Q):
  if Q:
    print(Q[-1])
  else:
    print("-1")

que = deque()

N = int(sys.stdin.readline())

for _ in range(N):
  M = sys.stdin.readline().split()
  if M[0] == "push":
    q_push(que, int(M[1]))
  elif M[0] == "pop":
    q_pop(que)
  elif M[0] == "front":
    q_front(que)
  elif M[0] == "back":
    q_back(que)
  elif M[0] == "empty":
    if que:
      print("0")
    else:
      print("1")
  else:
    print(len(que))
