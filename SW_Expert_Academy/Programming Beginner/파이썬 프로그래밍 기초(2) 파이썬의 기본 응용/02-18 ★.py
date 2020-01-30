num_list = list(map(int,input().split(',')))

num = [[i*j for i in range(num_list[1])] for j in range(num_list[0])]

print(num)