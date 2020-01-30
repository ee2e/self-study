num_list = list(map(int,input().split(',')))

odd_num = [num for num in num_list if num % 2 == 1]

print(", ".join(map(str,odd_num)))