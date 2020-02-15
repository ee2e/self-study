int_list = list(map(int,input().split()))

more_than = []
less_than = []

for integer in int_list:
    if integer >= 100:
        more_than.append(integer)
    else:
        less_than.append(integer)

def my_max(args):
    if len(args) == 0:
        return 100
    else:
        maximum = 0
        for i in range(len(args)):
            if args[i] > maximum:
                maximum = args[i]
        return maximum

def my_min(args):
    if len(args) == 0:
        return 100
    else:
        minimum = 0x7fffffffff
        for i in range(len(args)):
            if minimum > args[i]:
                minimum = args[i]
        return minimum
l = my_max(less_than)
m = my_min(more_than)

print('{} {}'.format(my_max(less_than),my_min(more_than)))