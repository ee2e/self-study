import sys

sys.stdin = open('4406.txt', 'r')

T = int(input())

for tc in range(T):
    string = input()

    vowel = ['a', 'e', 'i', 'o', 'u']
    result = ''

    for s in string:
        if s not in vowel:
            result += s

    print(f'#{tc+1} {result}')