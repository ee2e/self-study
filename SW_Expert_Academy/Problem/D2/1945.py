import sys
sys.stdin = open('1945.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    prime_numlist = [2, 3, 5, 7, 11]
    numlist = [0] * 5

    for idx, num in enumerate(prime_numlist):
        while N % num == 0:
            N /= num
            numlist[idx] += 1

    print(f'#{tc+1} {" ".join(map(str,numlist))}')