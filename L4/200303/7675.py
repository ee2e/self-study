import sys

sys.stdin = open('7675.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    sentence = input()
    
    length = []
    i = 0

    while i < len(sentence):
        name = []
        while sentence[i] != '.' and sentence[i] != '?' and sentence[i] != '!':
            if sentence[i].isupper():
                word = ''
                if i == 0 or (i-1 >= 0 and sentence[i-1] == ' '):
                    word += sentence[i]
                if i+1 < len(sentence):
                    while sentence[i+1].islower():
                        i += 1
                        word += sentence[i]
                    if len(word) != 0 and (sentence[i+1].isalpha() == False and sentence[i+1].isdecimal() == False):
                        name.append(word)
            if i+1 < len(sentence):
                i += 1
            else:
                break
        length.append(len(name))
        i += 1

    print(f'#{tc}', *length)