import sys
sys.stdin = open('2072.txt','r')

T = int(input())

for tc in range(T):
    num_list = list(map(int,input().split()))

    odd = [num for num in num_list if num % 2]

    s = sum(odd)

    print(f'#{tc+1} {s}')