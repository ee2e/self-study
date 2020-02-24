num = list(range(2,1000001))

num_list = []
for n in range(2,500001):
    for i in range(len(num)):
        if num[i] % n:
            num_list.append(num[i])
    
    if n == 500000:
        break
    num = num_list
    num_list = []

print(num_list)
