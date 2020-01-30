num_list = list(map(int,input().split(',')))

for i in range(len(num_list)):
    num_list[i] = round(2 * 3.141592 * num_list[i], 2)

# print(f'{num_list[0]} {num_list[1]} {num_list[2]} {num_list[3]}')
print(", ".join(map(str,num_list)))