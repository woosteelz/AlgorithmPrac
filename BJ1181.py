N = int(input())
answer = []

for _ in range(N):
  temp = str(input())
  if (temp, len(temp)) in answer:
    pass
  else:
    answer.append((temp, len(temp)))

answer.sort(key = lambda x:(x[1], x[0]))

for a in answer:
  print(a[0])