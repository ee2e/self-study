import sys
sys.stdin = open('2068.txt','r')

T = int(input())

for tc in range(T):
    num_list = list(map(int,input().split()))
    max = 0

    for i in range(len(num_list)):
        if num_list[i] > max:
            max = num_list[i]

    print(f'#{tc+1} {max}')