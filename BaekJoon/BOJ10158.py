w, h = map(int, input().split())
p, q = map(int, input().split())
time = int(input())

ans = []

if ((p + time) // w) % 2:  # 역방향일 경우
    ans.append(w - (p + time) % w)
else:  # 순방향일 경우
    ans.append((p + time) % w)

if ((q + time) // h) % 2:
    ans.append(h - (q + time) % h)
else:
    ans.append((q + time) % h)

print(*ans)
