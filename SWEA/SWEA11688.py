# SWEA 11688번 Calkin-Wilf tree 1
TC = int(input())

for tc in range(TC):
    dirs = input()
    top, bottom = 1, 1

    for dir in dirs:
        if dir == 'L':
            bottom = top + bottom
        else:
            top = top + bottom

    print(f'#{tc+1} {top} {bottom}')
