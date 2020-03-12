import sys

sys.stdin = open('특별한_정렬.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    array = list(map(int,input().split()))

    for i in range(N-1,0,-1):
        for j in range(0,i):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    array2 = []
    for i in range(N//2):
        array2.append(array[i])
        array2.append(array[-1-i])
    if N % 2:
        array2.append(array[N//2])
        
    array2 = array2[0:10]
    print(f'#{tc}', *array2)