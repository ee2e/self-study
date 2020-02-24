import sys

sys.stdin = open('cardgame.txt', 'r')

T = int(input())

def rsp(card):
    if len(card) <= 2:
        if len(card) == 1 or card[0][1] == card[1][1]:
            return card[0]
        elif card[0][1] == 1:
            if card[1][1] == 2:
                return card[1]
            else:
                return card[0]
        elif card[0][1] == 2:
            if card[1][1] == 3:
                return card[1]
            else:
                return card[0]
        else:
            if card[1][1] == 1:
                return card[1]
            else:
                return card[0]
    else:
        A = rsp(card[:(1+len(card))//2])
        B = rsp(card[(1+len(card))//2:])
        return rsp([A, B])



for tc in range(T):
    N = int(input())
    card = list(map(int,input().split()))
    idx = list(range(1,N+1))
    card = list(zip(idx,card))
    
    print(f'#{tc+1} {rsp(card)[0]}')