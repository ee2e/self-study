a, b, c = map(int,input().split())

if a > b and a > c:
    result1 = 1
else:
    result1 = 0

if a == b and b == c:
    result2 = 1
else:
    result2 = 0

print('{} {}'.format(result1,result2))