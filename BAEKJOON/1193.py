X = int(input())

result = 0
for x in range(1,X+1):
    if x*x//2 - x//2 + 1 > X:
        criteria = (x-1)*(x-1)//2 - (x-1)//2 + 1
        break
    elif x*x//2 - x//2 + 1 == X:
        if x&1:
            result = f'{x}/1'
        else:
            result = f'1/{x}'
        break
if not result:
    if (x-1)&1:
        result = f'{x-1-X+criteria}/{X-criteria+1}'
    else:
        result = f'{X-criteria+1}/{x-1-X+criteria}'

print(result)