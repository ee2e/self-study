import sys

sys.stdin = open('3143.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    A, B = input().split()

    A = A.replace(B, ' ', A.count(B))

    print(f'#{tc} {len(A)}')