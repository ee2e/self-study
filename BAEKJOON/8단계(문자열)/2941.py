string = input()

croatia_alpha = ['c=', 'c-', 'd-', 'li', 'nj', 's=', 'z=', 'dz=']
i = 0; cnt = 0
while i < len(string):
    if string[i:i+2] in croatia_alpha:
        i += 2
    elif string[i:i+3] in croatia_alpha:
        i += 3
    else:
        i += 1
    cnt += 1

print(cnt)