H, M = map(int,input().split())

if H == 0 and M < 45:
    time = 24*60+M-45
else:
    time = H*60+M-45

print(time//60, time%60)