'''
숫자에 대해 제곱을 구하는 함수를 정의히고, 다음과 같이 숫자를 콤마(,)로 구분해 입력하면
정의한 함수를 이용해 제곱 값을 출력하는 프로그램을 작성하십시오.

입력)
2, 3

출력)
square(2) => 4
square(3) => 9
'''
a, b = map(int,input().split(','))

def squ(*args):
    args_list = args
    for i in range(len(args_list)):
        if i != len(args_list)-1:
            print(f'square({args_list[i]}) => {args_list[i] ** 2}')
        else:
            return f'square({args_list[i]}) => {args_list[i] ** 2}'

print(squ(a, b))