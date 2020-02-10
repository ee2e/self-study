num_list = list(map(int,input().split()))

odd_cnt = 0
even_cnt = 0

for num in num_list:
    if num == 0:
        break
    elif num % 2:
        odd_cnt += 1
    else:
        even_cnt += 1

print('odd : {}'.format(odd_cnt))
print('even : {}'.format(even_cnt))