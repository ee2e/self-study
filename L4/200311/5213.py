import sys

sys.stdin = open('5213.txt', 'r')

T = int(input())

maxV = 10**6+1
temp = [0]*maxV
for i in range(1,maxV,2):
    for j in range(i,maxV,i):
        temp[j] += i

for i in range(1,maxV):
    temp[i] += temp[i-1]

result = []
for tc in range(1,T+1):
    L, R = map(int,input().split())
    ans = temp[R]-temp[L-1]
    result.append(f'#{tc} {ans}')

print('\n'.join(result))