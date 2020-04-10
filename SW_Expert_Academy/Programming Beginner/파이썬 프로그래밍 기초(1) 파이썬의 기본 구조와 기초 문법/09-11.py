'''
다음의 결과와 같이 'abcdef' 문자열의 각각의 문자를 키로 하고 0~5 사이의 정수를
값으로 하는 딕셔너리 객체를 생성하고, 이 딕셔너리 객체의 키와 값 정보를 출력하는
프로그램을 작성하십시오.

출력)
a: 0
b: 1
c: 2
d: 3
e: 4
f: 5
'''

str_list = list('abcdef')

str_dic = dict(zip(str_list,range(6)))

for key, val in str_dic.items():
    print(f'{key}: {val}')

# zip 함수