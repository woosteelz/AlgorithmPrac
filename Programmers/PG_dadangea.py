def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    graph_dict = dict(zip(enroll, range(len(enroll))))

    for i in range(len(seller)):
        curr = seller[i]
        price = amount[i] * 100
        while True:
            node_num = graph_dict[curr]
            income = price // 10
            answer[node_num] += price - income
            price = income
            curr = referral[node_num]
            if curr == "-":
                break
            if income == 0:
                break

    return answer
