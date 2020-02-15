num_list = list(map(int,input().split()))

cnt3 = 0
cnt5 = 0

for num in num_list:
    if num % 3 == 0:
        cnt3 += 1
    if num % 5 == 0:
        cnt5 += 1

print('Multiples of 3 : {}'.format(cnt3))
print('Multiples of 5 : {}'.format(cnt5))