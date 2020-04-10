word = input()

print(word)
for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        print('입력하신 단어는 회문(Palindrome)이 아닙니다.')
        break
else:
    print('입력하신 단어는 회문(Palindrome)입니다.')