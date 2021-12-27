def solution(n, k, cmd):
    table = ['O' for _ in range(n)]
    delete = ''
    curr = k

    while cmd:
        temp = cmd.pop(0)
        if temp[0] == 'U':
            idx = int(temp[1])
            while idx:
                curr -= 1
                if table[curr] == 'O':
                    idx -= 1

        elif temp[0] == 'D':
            idx = int(temp[1])
            while idx:
                curr += 1
                if table[curr] == 'O':
                    idx -= 1

        elif temp[0] == 'C':
            table[curr] = 'X'
            if curr == n - 1:
                while table[curr] == 'O':
                    curr -= 1
            else:
                while table[curr] == 'O':
                    curr += 1
