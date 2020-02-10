int_list = list(map(int,input().split()))

odd_list = []
even_list = []

for i in range(len(int_list)):
    if i % 2 == 0:
        odd_list.append(int_list[i])
    else:
        even_list.append(int_list[i])

print('sum : {}'.format(sum(even_list)))
print('avg : {:.1f}'.format(sum(odd_list)/len(odd_list)))