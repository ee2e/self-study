import sys

sys.stdin = open('special_array.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    int_list = list(map(int,input().split()))

    for i in range(10):
        for j in range(i,len(int_list)):
            if i % 2 == 0:
                if int_list[i] < int_list[j]:
                    int_list[i], int_list[j] = int_list[j], int_list[i]
            else:
                if int_list[i] > int_list[j]:
                    int_list[i], int_list[j] = int_list[j], int_list[i]

    result = ' '.join(map(str,int_list[:10]))
    print(f'#{tc+1} {result}')