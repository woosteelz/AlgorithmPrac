def solution(N, number):
    temp = str(N)
    arr = [set() for _ in range(9)]
    arr[1].add(N)
    if N == number:
        return 1
    for i in range(2, 9):
        print(arr)
        arr[i].add(int(temp*i))
        for j in range(1, i):
            for a in arr[i-j]:
                for b in arr[j]:
                    arr[i].add(a+b)
                    arr[i].add(abs(a-b))
                    if b != 0:
                        if not a % b:
                            arr[i].add(a//b)
                    arr[i].add(a*b)
                    if number in arr[i]:
                        return i
    return -1


solution(5, 12)
