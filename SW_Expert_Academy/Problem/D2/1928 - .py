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
    decimal_list = []

    for i in s_list:
        decimal_list.append(change(i))