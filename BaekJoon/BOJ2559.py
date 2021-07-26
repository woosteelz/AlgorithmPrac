# 2559번 수열

# 시간초과 O(n^2)
# n, k = map(int, input().split())
# temperature = list(map(int, input().split()))
# ans = []

# for i in range(n - k + 1):
#     ans.append(sum(temperature[i:i+k]))
# print(max(ans))

n, k = map(int, input().split())
temperature = list(map(int, input().split()))
ans = [sum(temperature[:k])]
temp = ans[0]
front = 0
back = k
for i in range(1, n-k+1):
    temp = temp - temperature[front] + temperature[back]
    front += 1
    back += 1
    ans.append(temp)
print(max(ans))
