def ari_sequence(num):
    global ari_sequence_list
    num = str(num)
    if 0 < len(num) < 2:
        ari_sequence_list[int(num)] = 1
        return
    else:
        d = int(num[1])-int(num[0])
        for i in range(1,len(num)-1):
            if int(num[i+1])-int(num[i]) != d:
                return
    ari_sequence_list[int(num)] = 1

ari_sequence_list = [0]*1001
for i in range(1,1001):
    ari_sequence(i)

N = int(input())

print(sum(ari_sequence_list[1:N+1]))