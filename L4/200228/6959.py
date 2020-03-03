import sys

sys.stdin = open('6959.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    num_list = [int(x) for x in input()]

    def game(num_list):
        temp = 0xfffffff
        for i in range(len(num_list)-1):
            if num_list[i] + num_list[i+1] > 10:
                temp = num_list[i] + num_list[i+1]
                idx = i
                break
            else:
                if num_list[i] + num_list[i+1] < temp:
                    idx = i
                    temp = num_list[i] + num_list[i+1]

        num_list.pop(idx+1); num_list.pop(idx)
        if temp >= 10:
            temp = str(temp)
            temp_list = [int(x) for x in temp]
            for x in range(1,-1,-1):
                num_list.insert(idx, temp_list[x])
        else:
            num_list.insert(idx,temp)

    cnt = 0
    while len(num_list) > 1:
        game(num_list)
        cnt += 1

    if cnt % 2:
        result = 'A'
    else:
        result = 'B'
    print(f'#{tc} {result}')