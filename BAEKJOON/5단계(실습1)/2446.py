N = int(input())

for i in range(-N+1,N):
    one = ' ' * (N-1-abs(i))
    two = '*' * (2*abs(i)+1)

    print(f'{one}{two}')