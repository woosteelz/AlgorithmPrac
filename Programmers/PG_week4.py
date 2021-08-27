def solution(table, languages, preference):
    answer = {
        'CONTENTS': 0,
        'GAME': 0,
        'HARDWARE': 0,
        'PORTAL': 0,
        'SI': 0,
    }

    # table 재저장
    for i in range(5):
        table[i] = list(map(str, table[i].split()))

    # 언어 / 언어별 선호도 접근
    for i in range(len(languages)):
        for j in range(5):
            if languages[i] in table[j]:
                answer[table[j][0]] += (6 - table[j].index(languages[i])) * preference[i]
                
    # 가장 높은 키 뽑기
    max_score = max(answer.values())
    ans = ''
    for key, value in answer.items():
        if value == max_score:
            ans = key
            break

    return ans


table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
         "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["PYTHON", "C++", "SQL"]
preference = [7, 5, 5]


print(solution(table, languages, preference))