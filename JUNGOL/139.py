N, M = map(int,input().split())

for i in range(1,10):
    for j in range(N,M-1,-1):
        print('{} * {} = {}'.format(j,i,i*j), end = '   ')
    print()