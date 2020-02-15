int_list = list(map(int,input().split()))

def bubble_sort(args):
    for j in range(len(args)-1,0,-1):
        for i in range(j):
            if args[i] < args[i+1]:
                args[i], args[i+1] = args[i+1], args[i]
    return args

print('{}'.format(' '.join(map(str,bubble_sort(int_list)))))