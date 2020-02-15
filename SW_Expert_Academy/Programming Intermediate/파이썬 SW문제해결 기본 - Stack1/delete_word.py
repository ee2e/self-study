import sys

sys.stdin = open('delete_word.txt','r')

T = int(input())

def CRTESTACK(): return []
def PUSH(stack,item): stack.append(item)
def POP(stack): return stack.pop(-1) if len(stack) else None
def ISEMPTY(stack): return len(stack) == 0
def PEEK(stack): return stack[-1] if len(stack) else None

for tc in range(T):
    word = [w for w in input()]

    word_stack = CRTESTACK()
    for w in word:
        if w == PEEK(word_stack):
            POP(word_stack)
        else:
            PUSH(word_stack,w)

    print(f'#{tc+1} {len(word_stack)}')