num = int(input())
num_list = [1]
number = 1
for i in range(num):
    number = number * 2
    num_list.append(number)

print(' '.join(map(str,num_list)))