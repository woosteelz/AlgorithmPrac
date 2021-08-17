def solution(scores):
    answer = ''
    scores = list(map(list, zip(*scores)))
    num = len(scores)
    for i in range(num):
        if (scores[i][i] == max(scores[i]) or scores[i][i] == min(scores[i])) and scores[i].count(scores[i][i]) == 1:
            answer += get_score((sum(scores[i]) - scores[i][i]) / (num - 1))
        else:
            answer += get_score(sum(scores[i]) / num)

    return answer


def get_score(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 50:
        return 'D'
    return 'F'
