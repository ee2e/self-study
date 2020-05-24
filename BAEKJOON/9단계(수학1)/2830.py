N = int(input())

result = 0
for x in range(N//5,-1,-1):
    N -= 5*x
    if N%3 == 0 and N//3 >= 0:
        y = N//3
        break
    N += 5*x
else:
    result = -1

print(result if result else x+y)