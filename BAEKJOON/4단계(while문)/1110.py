N = input()
if len(N) == 1:
    N = '0'+N

cnt = 0; new_N = N

while True:
    new_N = new_N[-1] + str(int(new_N[0])+int(new_N[1]))[-1]
    cnt += 1
    if N == new_N:
        break

print(cnt)