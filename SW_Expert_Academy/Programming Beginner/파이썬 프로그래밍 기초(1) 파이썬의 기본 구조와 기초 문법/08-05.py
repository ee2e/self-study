lis = [1, 2, 3, 4, 3, 2, 1]

def ret(args):
    args_set = set(args)
    args_list = list(args_set)
    return args_list

print(lis)
print(ret(lis))