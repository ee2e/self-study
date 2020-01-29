data = [2, 4, 6, 8, 10]

def find(num):
    if num in data:
        return True
    else:
        return False

print(data)
print(f'5 => {find(5)}')
print(f'10 => {find(10)}')