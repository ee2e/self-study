import copy

numbers = set({0,1})

plus_num = 3
while len(numbers) <= 10**10+1:
    temp_numbers = copy.deepcopy(numbers)
    for num in temp_numbers:
        numbers.add(num+plus_num)
    plus_num *= 3

print(numbers)