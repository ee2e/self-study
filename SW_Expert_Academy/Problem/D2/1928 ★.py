import sys
sys.stdin = open('1928.txt','r')

T = int(input())

def change(arg):
    val = list(range(64))
    string = list('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')
    result = 0

    for i in range(len(val)):
        if string[i] == arg:
            result = val[i]
    return result

for tc in range(T):
    s1 = input()
    s_list = list(s1)
    binary = ''
    decimal_list = []


    for i in s_list:
        binary += f'{str(bin(change(i)))[2:]:0>6}'

    for i in range(len(binary)//8):
        decimal_list.append((chr(int(binary[0+8*i:8+8*i],2))))

    print(f'#{tc+1} {"".join(decimal_list)}')