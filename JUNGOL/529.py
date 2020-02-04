height, weight = map(int,input().split())

if weight + 100 - height > 0:
    print(weight + 100 - height)
    print('Obesity')
else:
    print(weight + 100 - height)