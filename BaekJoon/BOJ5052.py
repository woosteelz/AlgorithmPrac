# 5052번 전화번호 목록
import sys
input = sys.stdin.readline


class Node:
    def __init__(self, data):
        self.data = data
        self.next = [None for _ in range(10)]


for _ in range(int(input())):
    N = int(input())
    nums = [input().strip() for _ in range(N)]
    nums.sort(key=lambda x: (len(x), x))

    print(nums)
