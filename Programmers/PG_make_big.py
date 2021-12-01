from collections import deque


def solution(number, k):
    answer = ''
    temp = []
    num = list(str(number))
    num = deque(num)
    num_len = len(num)
    while num:
        if not k:
            break

        n = int(num.popleft())

        if not temp:
            temp.append(n)
            continue

        while temp:
            if temp and temp[-1] >= n:
                break
            temp.pop(-1)
            k -= 1
            if not k:
                break
        temp.append(n)

    while num:
        temp.append(int(num.popleft()))

    for t in temp:
        answer += str(t)

    if not len(answer) == num_len - k:
        answer = answer[:num_len-k]

    return answer
