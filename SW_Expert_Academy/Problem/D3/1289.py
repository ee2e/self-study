import sys

sys.stdin = open('1289.txt', 'r')

T = int(input())

for tc in range(T):
    memory = input()
    
    comparison = '0'
    cnt = 0

    for i in range(len(memory)):
        if comparison != memory[i]:
            cnt += 1
            comparison = memory[i]

    print(f'#{tc+1} {cnt}')
