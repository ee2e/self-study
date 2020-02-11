import sys

sys.stdin = open('1221.txt', 'r')

T = int(input())

for tc in range(T):
    N, M = input().split()
    M = int(M)
    data = list(input().split())

    space_num = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
    earth_num = [0]*10

    for i in range(M):
        earth_num[space_num.index(data[i])] += 1

    print(N)
    for i in range(10):
        print(f'{space_num[i]}{(" " + space_num[i]) * (earth_num[i]-1)}', end = '')
        print(' ', end = '')
    print()