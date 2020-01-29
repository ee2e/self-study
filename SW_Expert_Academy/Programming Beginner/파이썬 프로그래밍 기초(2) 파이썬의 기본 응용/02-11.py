num_list = []
fibo = [num_list.append(num) if num == 0 or num == 1 else num_list.append(num_list[num-1]+num_list[num-2]) for num in range(11)]

print(num_list[1:])