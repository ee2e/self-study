num_list = list(map(int,input().split()))

def my_max(args):
    for j in range(len(args)-1,0,-1):
        for i in range(j):
            if args[i] > args[i+1]:
                args[i], args[i+1] = args[i+1], args[i]
    return args[0]

print(my_max(num_list))