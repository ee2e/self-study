import sys

sys.stdin = open('1208.txt','r')

def my_max(args):
    value = 0
    index = 0
    for idx, val in enumerate(args):
        if val >= value:
            value = val
            index = idx
    return value, index

def my_min(args):
    value = 0x7ffffffff
    index = 0
    for idx, val in enumerate(args):
        if val <= value:
            value = val
            index = idx
    return value, index


for tc in range(10):
    N = int(input())
    dump = list(map(int,input().split()))

    for _ in range(N):
        dump[my_max(dump)[1]] -= 1
        dump[my_min(dump)[1]] += 1

    result = my_max(dump)[0] - my_min(dump)[0]

    print('#{} {}'.format(tc+1,result))



