import sys

sys.stdin = open('forth.txt', 'r')

T = int(input())

for tc in range(T):
    code = list(input().split())

    stack = []

    for c in code:
        if c.isdecimal():
            stack.append(int(c))
        elif c == '.':
            result = stack.pop()
            if len(stack) != 0:
                result = 'error'
                break
        else:
            if len(stack) <= 1:
                result = 'error'
                break
            y = stack.pop()
            x = stack.pop()
            if c == '+':
                stack.append(x+y)
            elif c == '-':
                stack.append(x-y)
            elif c == '*':
                stack.append(x*y)
            elif c == '/':
                stack.append(x//y)

    print(f'#{tc+1} {result}')