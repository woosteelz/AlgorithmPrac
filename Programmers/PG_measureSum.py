def solution(left, right):
    ans = 0

    for num in range(left, right+1):
        temp = []
        for i in range(1, num + 1):
            if num % i == 0:
                temp.append(i)

        if len(temp) % 2:
            ans -= num
        else:
            ans += num

    return ans
