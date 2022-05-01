import sys

s = sys.stdin.readline().rstrip()
stack = []
tmp = 1
res = 0

for i in range(len(s)):
  if s[i] == '(':
    tmp *= 2
    stack.append(s[i])
  elif s[i] == '[':
    tmp *= 3
    stack.append(s[i])

  elif s[i] == ')':
    if not stack or stack[-1] == '[':
      res = 0
      break
    if s[i-1] == '(':
      res += tmp
    tmp //= 2
    stack.pop()
  
  else:
    if not stack or stack[-1] == '(':
      res = 0
      break
    if s[i-1] == '[':
      res += tmp
    tmp //= 3
    stack.pop()

if stack:
  res = 0
print(res)