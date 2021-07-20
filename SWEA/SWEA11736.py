# SWEA 11736번 평범한 숫자
TC = int(input())

for tc in range(TC):
    n = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(1, n-1):
        if arr[i] == max(arr[i-1:i+2]) or arr[i] == min(arr[i-1:i+2]):
            pass
        else:
            cnt += 1

    print(f'#{tc+1} {cnt}')
