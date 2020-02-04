import sys
sys.stdin = open('1284.txt','r')

T = int(input())

for tc in range(T):
    P,Q,R,S,W = map(int,input().split())

    A = W * P
    B = Q if W <= R else Q + (W-R) * S

    if A > B:
        result = B
    else:
        result = A

    print(f'#{tc+1} {result}')