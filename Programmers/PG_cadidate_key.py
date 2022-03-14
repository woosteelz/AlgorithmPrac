from itertools import combinations


def solution(relation):
    x, y = len(relation), len(relation[0])

    total = []
    for i in range(y):
        total += list(combinations([k for k in range(y)], i+1)) # 모든 조합 구하기

    uniq = []
    for t in total:
        temp = []
        for i in range(x):
            temp2 = []
            for j in t:
                temp2.append(relation[i][j])
            if not temp2 in temp:
                temp.append(temp2)
        if len(temp) == x:
            uniq.append(t)
    
    ans = uniq[:]
    for i in range(len(uniq)):
        for j in range(i+1, len(uniq)):
            if len(uniq[i]) == len(set(uniq[i]).intersection(set(uniq[j]))):
                if uniq[j] in ans:
                    ans.remove(uniq[j])
    
    return len(ans)