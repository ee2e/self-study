import sys

sys.stdin = open('7701.txt', 'r')

T = int(input())

result = []
for tc in range(1,T+1):
    N = int(input())
    names = set()

    for _ in range(N):
        temp = input()
        names.add((len(temp),temp))

    names = list(names)
    names.sort()

    result.append(f'#{tc}')
    for i in range(len(names)):
        result.append(names[i][1])

print('\n'.join(result))