import sys
sys.stdin = open('2029.txt', 'r')

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())
    num1 = a // b
    num2 = a % b
    print(f'#{tc+1} {num1} {num2}')