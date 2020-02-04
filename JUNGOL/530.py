age = int(input())

if age >= 20:
    print('adult')
else:
    num = 20 - age
    print('{} years later'.format(num))