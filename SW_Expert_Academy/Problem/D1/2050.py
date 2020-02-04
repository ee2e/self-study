s = input()
s_list = list(s)
num_list = []

for i in range(len(s_list)):
    num_list.append(ord(s_list[i])-64)

print(' '.join(map(str,num_list)))