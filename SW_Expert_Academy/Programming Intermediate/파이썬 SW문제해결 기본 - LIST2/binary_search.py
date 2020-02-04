import sys

sys.stdin = open('binary_search.txt','r')

T = int(input())

def book_search(a, s):
    left = 1
    right = a
    result = 0
    while s != (left+right)//2:
        if (left+right)//2 > s:
            right = (left+right)//2
        else:
            left = (left+right)//2
        result += 1
    return result

for tc in range(T):
    P, A, B = map(int, input().split())
    if book_search(P,A) < book_search(P,B):
        result = 'A'
    elif book_search(P,A) > book_search(P,B):
        result = 'B'
    else:
        result = 0

    print(f'#{tc+1} {result}')
