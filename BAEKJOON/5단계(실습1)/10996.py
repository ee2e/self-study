N = int(input())

a = (N-1)//2
b = N//2

one = f'{"* " * (a+1)}'
two = f'{" *" * b}'

for _ in range(N):
    print(f'{one}\n{two}')