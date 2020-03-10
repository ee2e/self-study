import sys

sys.stdin = open('4047.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    card = input()
    cardlist = []

    result = 0
    for i in range(0,len(card),3):
        if card[i:i+3] in cardlist:
            result = 'ERROR'
        else:
            cardlist.append(card[i:i+3])

    check = [13]*4
    if result:
        pass
    else:
        for i in range(len(cardlist)):
            if cardlist[i][0] == 'S':
                check[0] -= 1
            elif cardlist[i][0] == 'D':
                check[1] -= 1
            elif cardlist[i][0] == 'H':
                check[2] -= 1
            else:
                check[3] -= 1
        result = ' '.join(map(str,check))

    print(f'#{tc}', result)