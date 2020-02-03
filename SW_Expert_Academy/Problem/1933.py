N = int(input())
div_list = []

for i in range(1,N+1):
    if N % i == 0:
        div_list.append(i)

print(' '.join(map(str,div_list)))