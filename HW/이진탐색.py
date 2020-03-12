import sys

sys.stdin = open('이진탐색.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    P, A, B = map(int,input().split())

    Al = Bl = 1
    Ar = Br = P

    cA = cB = 0
    while cA != A and cB != B:
        cA = int((Al+Ar)/2)
        if cA == A: pass
        elif cA < A: Al = cA
        else: Ar = cA
        cB = int((Bl+Br)/2)
        if cB == B: pass
        elif cB < B: Bl = cB
        else: Br = cB
    
    result = 0 if cA == A and cB == B else 'A' if cA == A else 'B'

    print(f'#{tc}', result)