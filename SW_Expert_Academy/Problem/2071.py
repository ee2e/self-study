import sys
sys.stdin = open('2071.txt', 'r')

T = int(input())

for tc in range(T):
    num_list = list(map(int,input().split()))

    average = sum(num_list)/len(num_list)

    print(f'#{tc+1} {round(average,0):.0f}')