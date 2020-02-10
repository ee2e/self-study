num_list = list(map(int, input().split()))

num_cnt = 0

for num in num_list:
    if num % 3 != 0 and num % 5 != 0:
        num_cnt += 1
    elif num == 0:
        break

print(num_cnt)