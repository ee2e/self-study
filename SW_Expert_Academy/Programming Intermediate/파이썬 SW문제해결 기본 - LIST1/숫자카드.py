import sys
sys.stdin = open('숫자카드.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    data = input()
    data_dict = {}
    ans = 0
    result = 0

    for i in range(N):
        if data[i] not in data_dict:
            data_dict[data[i]] = 1
        else:
            data_dict[data[i]] += 1
    
    for key, val in data_dict.items():
        if ans < val:
            ans = val
            result = key
    
    if ans == 1:
        for key in data_dict.keys():
            if result < key:
                result = key

    print("#{} {} {}".format(tc+1, result, ans))