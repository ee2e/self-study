string = input()
string = string.upper()

str_num = [0]*26

for s in string:
    str_num[ord(s)-65] += 1

maxV = 0; index = 0; max_list = []
for i in range(26):
    if str_num[i] >= maxV:
        max_list.append(str_num[i])
        maxV = str_num[i]
        index = i

if len(max_list) > 1:
    if max_list[-1] == max_list[-2]:
        result = '?'
    else:
        result = chr(index+65)
else:
    result = chr(index+65)

print(result)