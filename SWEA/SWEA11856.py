# SWEA 11856번 반반
TC = int(input())

for tc in range(TC):
    word = input()
    word_set = list(set(list(word)))

    if not len(word_set) == 2:
        print(f'#{tc+1} No')
        continue

    if not word.count(word_set[0]) == 2:
        print(f'#{tc+1} No')
        continue

    if not word.count(word_set[1]) == 2:
        print(f'#{tc+1} No')
        continue

    print(f'#{tc+1} Yes')
