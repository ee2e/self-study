import sys

sys.stdin = open('1926.txt','r')

N = int(input())
num_list = []

for i in range(1,N+1):
    s = str(i)
    s_list = list(s)

    cnt = 0
    for j in range(len(s_list)):
        if int(s_list[j]) % 3 == 0 and int(s_list[j]) != 0:
            cnt += 1
        
    for k in range(cnt+1):
        if cnt == 0:
            pass
        elif cnt == k:
            s_list = '-'*k

    num_list.append(s_list)

for i in range(N-1):
    print(''.join(num_list[i]), end = ' ')
print(''.join(num_list[N-1]))