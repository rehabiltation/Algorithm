# 소요시간: 10분
# 특이사항: stack and 까먹지좀말라!!!!

parenthesis = list(input())
stack = []

for p in parenthesis:
    if p == '(':
        stack.append('(')
    elif stack and stack[-1] == '(' and p == ')':
        stack.pop()
    else:
        stack.append(')')

print(len(stack))
