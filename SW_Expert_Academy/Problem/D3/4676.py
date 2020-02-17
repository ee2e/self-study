import sys

sys.stdin = open('4676.txt', 'r')

T = int(input())

for tc in range(T):
    string = [x for x in input()]
    H = int(input())
    position = list(map(int,input().split()))

    position.sort()

    for i in range(H-1,-1,-1):
        string.insert(position[i], '-')

    print(f'#{tc+1} {"".join(string)}')