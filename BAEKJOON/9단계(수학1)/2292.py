N = int(input())

cnt = 0
for x in range(1,N+1):
    if 3*x*x - 3*x + 1 < N:
        cnt += 1
    else:
        cnt += 1
        break

print(cnt)