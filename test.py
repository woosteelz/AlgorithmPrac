def solution(curr, cnt, length):
    global ans
    if curr == [0, N-1]:
        ans = min(ans, cnt)
        return


for tc in range(int(input())):
    ans = -1
    M, N, L = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(M)]

    print(ans)
