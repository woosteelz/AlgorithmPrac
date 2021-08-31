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

for tc in range(int(input())):
    n = int(input())
    led = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if led[i] == 1:
            k, idx = i + 1, i + 1
            while idx <= n:
                if led[idx - 1] == 1:
                    led[idx - 1] = 0
                else:
                    led[idx - 1] = 1
                idx += k
            cnt += 1
        if sum(led) == 0:
            break

    print('#{} {}'.format(tc+1, cnt))
