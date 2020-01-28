num = list()

for i in range(100,301) :
    if (i // 100) % 2 == 0 :
        if (i // 10) % 2 == 0 :
            if i % 2 == 0 :
                num.append(str(i))

print(','.join(num))
