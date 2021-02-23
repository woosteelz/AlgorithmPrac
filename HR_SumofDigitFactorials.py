# HackerRank Sums of Digit Factorials

def factorial(n):
  if n > 1:
    return n * factorial(n-1)
  else:
    return 1
    
def factorial_adv(n):
  result = 0
  while n:
    result += factorial(n%10)
    n //= 10
  return result

def sum_digit(n):
  result = 0
  while n:
    result += n%10
    n //= 10
  return result

TC = int(input())

for _ in range(TC):
  N, M = map(int, input().split())
  result = 0
  for i in range(1, N+1):
    temp = sum_digit(factorial_adv(i))
    for j in range(1, i+1):
      if sum_digit(factorial_adv(j)) == temp:
        result += sum_digit(j)
        print(j)
        break

  print(result)
