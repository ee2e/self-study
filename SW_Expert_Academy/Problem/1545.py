num = int(input())
num_list = []
for i in range(num,-1,-1):
    num_list.append(i)
print(' '.join(map(str,num_list)))