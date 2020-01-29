def mul(*args):
    args_list = list(args)
    result = 1
    for i in args_list:
        if type(i) == int:
            result *= i
        else:
            return '에러발생'
    return result

print(mul(1, 2, '4', 3))
