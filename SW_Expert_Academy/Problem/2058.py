num = input()
num_list = list(num)
result = 0

for i in range(len(num_list)):
    result += int(num_list[i])

print(result)