import sys

sys.stdin = open('2948.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    str_list1 = list(input().split())
    str_list2 = list(input().split())

    new_list = str_list1 + str_list2

    K = len(set(new_list))

    print(f'#{tc} {N+M-K}')