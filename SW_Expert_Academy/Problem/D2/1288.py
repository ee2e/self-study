import sys
sys.stdin = open('1288.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    num_list = [0] * 10
    i = 0
    summ = 0

    while summ != 10:
        i += 1
        summ = 0
        st = str(N*i)
        for s in st:
            num_list[int(s)] += 1

        for j in range(10):
            if num_list[j] >= 1:
                summ += 1

    print(f'#{tc+1} {N*i}')