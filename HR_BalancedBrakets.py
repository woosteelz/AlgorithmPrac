# HackerrRank Balanced Brackets (Medium)

def isBalanced(s):
  stack = []
  s = list(s)
  for i in s:
    print(stack)
    if i == "{" or i == "(" or i == "[":
      stack.append(i)
    else:
      if not stack:
        return "NO"
      temp = stack.pop(-1)
      if i == ")" and not temp == "(":
        return "NO"
      elif i == "}" and not temp == "{":
        return "NO"
      elif i == "]" and not temp == "[":
        return "NO"

  if stack:
    return "NO"
  else:
    return "YES"

print(isBalanced("{{[[(())]]}}"))
      