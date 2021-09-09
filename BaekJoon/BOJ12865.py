# 12865번 평범한 배낭
import pprint

N, K = map(int, input().split())
weight, price = [], []
for _ in range(N):
    w, p = map(int, input().split())
    weight.append(w)
    price.append(p)

ans = [[0 for _ in range(K)] for _ in range(N)]

for i in range(N):
    for w in range(K):
        if weight[i] <= w:
            ans[i][w] = max(price[i] + ans[i][w], ans[i][w])
        else:
            ans[i][w] = ans[i-1][w]

pprint.pprint(ans)

print(ans[N-1][K-1])


'''
for w = 0 to W
    b[0, w] = 0
for i = 0 to N
    b[i, 0] = 0
    for w = 0 to W
        if w_i <= w
            if b_i + b[i-1, w-w_i] > b[i - 1, w]
                b[i, w] = b_i + b[i-1, w-w_i]
            else
                b[i, w] = b[i-1, w]
        else
            b[i, w] = b[i-1, w]
'''
