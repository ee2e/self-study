# judge = input()

# letters = 0
# digits = 0
# for i in range(len(judge)):
#     if judge[i].isalpha():
#         letters += 1
#     elif judge[i].isdigit():
#         digits += 1

# print('LETTERS', letters)
# print('DIGITS', digits)

word = input()

judge = {
    'LETTERS': 0,
    'DIGITS': 0
}

for i in range(len(word)):
    if word[i].isalpha():
        judge['LETTERS'] += 1
    elif word[i].isdigit():
        judge['DIGITS'] += 1

for key, value in judge.items():
    print(key, value)