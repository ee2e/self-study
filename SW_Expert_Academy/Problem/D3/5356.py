import sys

sys.stdin = open('5356.txt', 'r')

T = int(input())

for tc in range(T):
    data = [input() for _ in range(5)]

    string = ''
    len_max = 0
    for i in range(5):
        if len(data[i]) > len_max:
            len_max = len(data[i])
    
    for m in range(len_max):
        for i in range(5):
            if len(data[i]) > m:
                string += data[i][m]

    print(f'#{tc+1} {string}')