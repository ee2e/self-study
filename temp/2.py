import sys

sys.stdin = open('2.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    answer_sheet = input()
    sheets = list(map(str,input().split('","')))

    print(sheets)