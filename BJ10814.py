N = int(input())
db = []
for i in range(N):
  age, name = map(str, input().split())
  db.append((int(age), i, name))
db.sort(key = lambda x:(x[0], x[1]))

for i in range(N):
  print(db[i][0], db[i][2])