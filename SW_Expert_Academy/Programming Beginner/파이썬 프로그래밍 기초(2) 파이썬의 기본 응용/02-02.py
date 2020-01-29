'''
리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

출력)
Pythn s pwrfl... nd fst; plys wll wth thrs; rns vrywhr; s frndly & sy t lrn; s Opn.
'''
str_list = list('Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.')

vowel = ['a','e','i','o','u']

new_list = []

new_list = [j for j in str_list if j not in vowel]

print(''.join(new_list))