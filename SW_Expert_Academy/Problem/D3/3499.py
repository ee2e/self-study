import sys

sys.stdin = open('3499.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    order = input().split()

    if len(order) % 2:
        order1 = order[:len(order)//2+1]
        order2 = order[len(order)//2+1:]
    else:
        order1 = order[:len(order)//2]
        order2 = order[len(order)//2:]
    
    result = []
    for i in range(len(order1)):
        result.append(order1[i])
        if len(order2) > i:
            result.append(order2[i])

    print(f'#{tc+1} {" ".join(result)}')