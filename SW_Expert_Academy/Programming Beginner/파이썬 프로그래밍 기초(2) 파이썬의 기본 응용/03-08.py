words = input()

judge = {
    'UPPER CASE': 0,
    'LOWER CASE': 0
}

for word in words:
    if word.isupper():
        judge['UPPER CASE'] += 1
    elif word.islower():
        judge['LOWER CASE'] += 1

for key, value in judge.items():
    print(key, value)