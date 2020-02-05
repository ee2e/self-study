import sys

sys.stdin = open('1989.txt','r')

T = int(input())

def palindrome(args):
    r = list(reversed(args))
    if args == r:
        return 1
    else:
        return 0

for tc in range(T):
    s = input()
    s_list = list(s)

    print(f'#{tc+1} {palindrome(s_list)}')

