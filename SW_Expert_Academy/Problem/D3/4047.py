import sys

sys.stdin = open('4047.txt', 'r')

T = int(input())

for tc in range(T):
    card_dummy = input()
    card_list = []

    for i in range(0,len(card_dummy),3):
        card_list.append(card_dummy[i:i+3])

    S_num = [0]*14
    D_num = [0]*14
    H_num = [0]*14
    C_num = [0]*14

    result = 0
    for i in range(len(card_list)):
        if card_list[i][0] == 'S':
            if S_num[int(card_list[i][1:])]:
                result = 'ERROR'
                break
            S_num[int(card_list[i][1:])] = 1
        if card_list[i][0] == 'D':
            if D_num[int(card_list[i][1:])]:
                result = 'ERROR'
                break
            D_num[int(card_list[i][1:])] = 1
        if card_list[i][0] == 'H':
            if H_num[int(card_list[i][1:])]:
                result = 'ERROR'
                break
            H_num[int(card_list[i][1:])] = 1
        if card_list[i][0] == 'C':
            if C_num[int(card_list[i][1:])]:
                result = 'ERROR'
                break
            C_num[int(card_list[i][1:])] = 1

    if not result:
        result = f'{13-sum(S_num)} {13-sum(D_num)} {13-sum(H_num)} {13-sum(C_num)}'
    
    print(f'#{tc+1} {result}')