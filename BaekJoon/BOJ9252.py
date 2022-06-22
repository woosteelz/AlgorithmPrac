# 9252 LCS 2

from pprint import pprint


def longest_common_subsequence(s1, s2):
    m, n = len(s2), len(s1)
    LCS = [[0 for _ in range(m+1)] for _ in range(n+1)] # 2차원 배열 초기화
    s1, s2 = ' ' + s1, ' ' + s2 # 마진값
	
    for i in range(1, n+1):
        for j in range(1, m+1):
            if not s1[j] == s2[i]:
                LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])
            else:
                LCS[i][j] = LCS[i-1][j-1] + 1

    i, j = n, m
    ans = ''
    while i > 0 and j > 0:
        if LCS[i][j-1] == LCS[i][j]:
            j -= 1
        elif LCS[i-1][j] == LCS[i][j]:
            i -= 1
        else:
            ans = s1[j] + ans
            i -= 1
            j -= 1
    return max(map(max, LCS)), ans

s1 = input()
s2 = input()

length, string = longest_common_subsequence(s1, s2)
if length:
    print(length)
    print(string)
else:
    print(length)

