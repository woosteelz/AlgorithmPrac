import sys
import heapq
input = sys.stdin.readline

left, right = [], []

N = int(input())
for _ in range(N):
    # 양쪽 리스트에 하나씩 번갈아가며 삽입: 왼쪽 리스트는 최대 힙으로 구성해야 첫번째 원소가 중간값이 됨
    if len(left) == len(right):
        heapq.heappush(left, -int(input()))
    else:
        heapq.heappush(right, int(input()))
    
    # 왼쪽 리스트의 첫번째 원소가 오른쪽 리스트의 첫번째 원소보다 작다면 중간값이 꺠져버리므로 바꾸어서 넣어줌
    if left and right and right[0] < -left[0]:
        left_val = heapq.heappop(left)
        right_val = heapq.heappop(right)
        heapq.heappush(left, -right_val)
        heapq.heappush(right, -left_val)
    print(-left[0])