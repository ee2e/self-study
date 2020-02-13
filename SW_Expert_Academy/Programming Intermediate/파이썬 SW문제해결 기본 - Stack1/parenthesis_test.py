import sys

sys.stdin = open('parenthesis_test.txt','r')

T = int(input())

for tc in range(T):
    code = input()

    def CRTESTACK() : return []
    def PUSH(stack, item) : stack.append(item)
    def ISEMPTY(stack) : return len(stack) == 0
    def POP(stack) : return stack.pop(-1) if len(stack) else None
    def PEEK(stack) : return stack[-1] if len(stack) else None

    par_stack = CRTESTACK()

    result = 1
    for c in code:
        if c == '(':
            PUSH(par_stack,c)
        elif c == '{':
            PUSH(par_stack,c)
        elif c == ')':
            if POP(par_stack) != '(':
                result = 0
                break
        elif c == '}':
            if POP(par_stack) != '{':
                result = 0
                break

    if ISEMPTY(par_stack) == False:
        result = 0

    print(f'#{tc+1} {result}')