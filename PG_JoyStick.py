# Programmers JoyStick

# 조이스틱을 왼쪽으로 옮겼을 때 소요 비용과 인덱스 반환
def go_left(index, name):
  cnt = 0
  while True:
    index -= 1
    cnt += 1
    if index == -1:
      index = len(name)-1
    if name[index]:
      break
  return cnt, index

# 조이스틱을 오른쪽으로 옮겼을 때 소요 비용과 인덱스 반환
def go_right(index, name):
  cnt = 0
  while True:
    index += 1
    cnt += 1
    if index == len(name):
      index = 0
    if name[index]:
      break
  return cnt, index

def solution(name):
  name = list(name)

  # name을 배열로 변환 후 소요 비용 전 처리
  for i in range(len(name)):
    if ord(name[i]) - 65 > 13:
      name[i] = abs(ord(name[i]) - 65 - 26)
    else:
      name[i] = ord(name[i]) - 65
  answer = 0
  index = 0

  while True:
    answer += name[index]
    name[index] = 0

    # name의 모든 요소가 0가 되면 while문 탈출
    if sum(name) == 0:
      break

    left = go_left(index, name)
    right = go_right(index, name)

    if left[0] >= right[0]:
      answer += right[0]
      index = right[1]
    else:
      answer += left[0]
      index = left[1]

  return answer

print(solution('JEROEN'))