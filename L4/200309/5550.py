import sys

sys.stdin = open('5550.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    crying = input() #croak

    C = []
    R = []
    O = []
    A = []
    flag = result = 0
    for i in crying:
        if i == 'c':
            C.append(i)
        elif i == 'r':
            if len(C) != 0:
                C.pop()
                R.append(i)
            else:
                flag = 1
                break
        elif i == 'o':
            if len(R) != 0:
                R.pop()
                O.append(i)
            else:
                flag = 1
                break
        elif i == 'a':
            if len(O) != 0:
                O.pop()
                A.append(i)
            else:
                flag = 1
                break
        else:
            if len(A) != 0:
                A.pop()
                result += 1
            else:
                flag = 1
                break

    
    i = cnt = 0
    com = 'croak'
    while i < len(crying):
        j = 0
        while j < 4:
            if crying[i] == com[j]:
                i += 1
                j += 1
            else:
                i += 1
            if i == len(crying)-1:
                break
        while j != 5:
            if crying[i] == com[j]:
                cnt += 1
                j += 1
            else:
                i += 1
    
    if flag or (len(C) != 0 or len(R) != 0 or len(O) != 0 or len(A) != 0):
        result = -1

    print(result, cnt)