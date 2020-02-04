import sys

sys.stdin = open('1966.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num_list = list(map(int,input().split()))

    num_list.sort()

    print(f'#{tc+1} {" ".join(map(str,num_list))}')