import sys

sys.stdin = open('글자수.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    
    maxV = 0
    for i in range(len(str1)):
        temp = str2.count(str1[i])
        if temp > maxV:
            maxV = temp

    print(f'#{tc}', maxV)