'''
ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

입력)
65

출력)
ASCII 65 => A
'''

arg = int(input())

def trans(num):
    return chr(num)

print(f'ASCII {arg} => {trans(arg)}')