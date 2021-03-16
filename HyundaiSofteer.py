import sys

N = int(sys.stdin.readline())
A = []
B = []
moveAtoB = []
moveBtoA = []
for _ in range(N - 1):
    a, b, c, d = map(int, sys.stdin.readline().split())
    A.append(a)
    B.append(b)
    moveAtoB.append(c)
    moveBtoA.append(d)
a, b = map(int, sys.stdin.readline().split())
A.append(a)
B.append(b)

ansA = ['a', A[0]]
ansB = ['b', B[0]]

for i in range(N - 1):
    if ansA[0] == 'a':
        if B[i + 1] + moveAtoB[i] < A[i + 1]:
            ansA[0] = 'b'
            ansA[1] += B[i + 1] + moveAtoB[i]
        else:
            ansA[1] += A[i + 1]
    elif ansA[0] == 'b':
        if A[i + 1] + moveBtoA[i] < B[i + 1]:
            ansA[0] = 'a'
            ansA[1] += A[i + 1] + moveBtoA[i]
        else:
            ansA[1] += B[i + 1]
    
    if ansB[0] == 'a':
        if B[i + 1] + moveAtoB[i] < A[i + 1]:
            ansB[0] = 'b'
            ansB[1] += B[i + 1] + moveAtoB[i]
        else:
            ansB[1] += A[i + 1]
    elif ansB[0] == 'b':
        if A[i + 1] + moveBtoA[i] < B[i + 1]:
            ansB[0] = 'a'
            ansB[1] += A[i + 1] + moveBtoA[i]
        else:
            ansB[1] += B[i + 1]

print(ansA[1], ansB[1])
