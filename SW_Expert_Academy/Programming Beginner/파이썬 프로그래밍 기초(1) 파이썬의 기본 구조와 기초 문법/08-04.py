num = int(input())

def fibo(num):
    fibo_list = []
    for i in range(num+1):
        if i == 0 or i == 1:
            fibo_list.append(i)
        else:
            n = fibo_list[i-1] + fibo_list[i-2]
            fibo_list.append(n)
    return fibo_list[1:]

print(fibo(num))