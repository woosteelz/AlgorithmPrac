# SWEA 11445번 무한 사전
TC = int(input())

for tc in range(TC):
    p = input().strip()
    q = input().strip()

    if p == q:
        print(f'#{tc+1} N')
    elif p + 'a' == q:
        print(f'#{tc+1} N')
    else:
        print(f'#{tc+1} Y')
