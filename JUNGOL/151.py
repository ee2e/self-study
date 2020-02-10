int_list = list(map(int,input().split()))

sum = 0
for i in range(len(int_list)):
    if i % 2 == 0:
        sum += int_list[i]

print(sum)