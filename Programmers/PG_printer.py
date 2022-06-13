def solution(priorities, location):
    answer = 0
    
    while len(priorities) > 0:
        maxPri = max(priorities)
        if priorities[0] < maxPri:
            priorities.append(priorities[0])
            priorities.pop(0)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
        elif priorities[0] == maxPri:
            priorities.pop(0)
            answer += 1
            if location == 0:
                break
            else:
                location -= 1

    return answer
