import sys

sys.stdin = open('4789.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    clap = input()

    people = int(clap[0])
    cnt = 0
    for i in range(1,len(clap)):
        if people >= i:
            people += int(clap[i])
        else:
            cnt += i - people
            people += i - people + int(clap[i])

    print(f'#{tc} {cnt}')