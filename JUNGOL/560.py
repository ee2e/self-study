int_list = list(map(int,input().split()))

def my_min(args):
    minimum = args[0]
    for i in range(1, len(int_list)):
        if minimum > args[i]:
            minimum = args[i]
    return minimum

print(my_min(int_list))