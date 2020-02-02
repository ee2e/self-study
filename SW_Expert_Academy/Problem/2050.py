'''
알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.


[제약 사항]

문자열의 최대 길이는 200이다.


[입력]

알파벳으로 이루어진 문자열이 주어진다.


[출력]

각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.
'''
s = input()
s_list = list(s)
num_list = []

for i in range(len(s_list)):
    num_list.append(ord(s_list[i])-64)

print(' '.join(map(str,num_list)))