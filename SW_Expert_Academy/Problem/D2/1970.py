import sys

sys.stdin = open('1970.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())

    amount = []

    for i in range(8,0,-1):
        if i % 2 == 0:
            num = 5 * (10 ** (i//2))
        else:
            num = 10 ** (i//2+1)
        
        amount.append(N//num)
        N -= num * (N//num)

    print(f'#{tc+1}')
    print(f'{" ".join(map(str,amount))}')