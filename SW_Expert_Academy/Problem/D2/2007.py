import sys

sys.stdin = open('2007.txt','r')

T = int(input())

for tc in range(T):
    s = input()
    s_list = list(s)
    word = ''

    for i in range(len(s_list)):
        if i == 0:
            word += s_list[i]
        else:
            if s_list[i] == s_list[0] and s_list[i+1] == s_list[1] and s_list[i+2] == s_list[i+2]:
                break
            else:
                word += s_list[i]

    print(f'#{tc+1} {len(word)}')