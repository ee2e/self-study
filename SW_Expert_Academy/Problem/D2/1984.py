import sys

sys.stdin = open('1984.txt','r')

T = int(input())

for tc in range(T):
    num_list = list(map(int,input().split()))

    num_list.remove(max(num_list))
    num_list.remove(min(num_list))

    result = int(round(sum(num_list) / len(num_list),0))

    print(f'#{tc+1} {result}')