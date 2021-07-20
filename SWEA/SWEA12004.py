# SWEA 12004번 구구단 1
import sys


def is_posisible(num):
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == num:
                return True
    return False


TC = int(sys.stdin.readline())

for tc in range(TC):
    num = int(sys.stdin.readline())
    if is_posisible(num):
        print(f'#{tc+1} Yes')
    else:
        print(f'#{tc+1} No')
