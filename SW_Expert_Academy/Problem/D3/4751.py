import sys

sys.stdin = open('4751.txt', 'r')

T = int(input())

for tc in range(T):
    string = input()

    s0 = '.'
    s1 = '.'
    s2 = '#'
    
    for s in string:
        s0 += '.#..'
        s1 += '#.#.'
        s2 += '.' + s + '.#'

    print(s0, s1, s2, s1, s0, sep = '\n')