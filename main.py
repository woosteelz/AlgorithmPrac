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

def pre_order(n):
    if n:
        print(n)
        pre_order(left[n])
        pre_order(right[n])

V = 13
temp = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]

left = [0 for _ in range(V+1)]
right = [0 for _ in range(V+1)]

for i in range(V-1):
    parent, child = temp[i*2], temp[i*2+1]
    if not left[parent]:
        left[parent] = child
    else:
        right[parent] = child

pre_order(1)