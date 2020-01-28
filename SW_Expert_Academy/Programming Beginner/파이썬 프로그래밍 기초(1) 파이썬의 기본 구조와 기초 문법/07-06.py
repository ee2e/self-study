blood_types = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

cnt_a = cnt_b = cnt_o = cnt_ab = 0

for blood in blood_types :
    if blood == 'A' :
        cnt_a += 1
    elif blood == 'B' :
        cnt_b += 1
    elif blood == 'O' :
        cnt_o += 1
    else :
        cnt_ab += 1

cnt = {'A': cnt_a, 'O': cnt_o, 'B': cnt_b, 'AB': cnt_ab}
print(cnt)