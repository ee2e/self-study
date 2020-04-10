words = 'abcdefgabc'

word_dict = {}

for word in words:
    if word_dict.get(word):
        word_dict[word] += 1
    else:
        word_dict[word] = 1

for key, value in word_dict.items():
    print(f'{key},{value}')