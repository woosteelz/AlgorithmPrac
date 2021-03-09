# HackerrRank A Tale of Two Stacks

# 초기 상태
# class MyQueue(object):
#     def __init__(self):
        
    
#     def peek(self):
        
        
#     def pop(self):
        
        
#     def put(self, value):
        

# queue = MyQueue()
# t = int(input())
# for line in range(t):
#     values = map(int, input().split())
#     values = list(values)
#     if values[0] == 1:
#         queue.put(values[1])        
#     elif values[0] == 2:
#         queue.pop()
#     else:
#         print(queue.peek())

class MyQueue(object):
  def __init__(self):
    self.FIFO = []
  def peek(self):
    return self.FIFO[0]
  def pop(self):
    self.FIFO.pop(0)    
  def put(self, value):
    self.FIFO.append(value)
  def showQueue(self):
    print(self.FIFO)

queue = MyQueue()
t = int(input())
for line in range(t):
  values = map(int, input().split())
  values = list(values)
  if values[0] == 1:
    queue.put(values[1])        
  elif values[0] == 2:
    queue.pop()
  else:
    print(queue.peek())
  queue.showQueue()
      