num_list = list(map(int,input().split()))

for i in range(len(num_list)):
    if num_list[i] != 0:
        num_list[i] = True
    else:
        num_list[i] = False

print('{} {}'.format(int(num_list[0] and num_list[1]), int(num_list[0] or num_list[1])))