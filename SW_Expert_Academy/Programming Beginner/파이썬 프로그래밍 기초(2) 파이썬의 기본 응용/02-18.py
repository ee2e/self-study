num1, num2 = map(int,input().split(','))

num = [[i*j for i in range(num2)] for j in range(num1)]

print(num)