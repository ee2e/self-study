num = list()

for i in range(1,101) :
    if i % 2 :
        num.append(str(i))

print(', '.join(num))