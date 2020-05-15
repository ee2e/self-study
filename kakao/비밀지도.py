import sys

sys.stdin = open('비밀지도.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    array1 = list(map(int,input().split()))
    array2 = list(map(int,input().split()))

    password = ['']*N
    for i in range(N):
        num = array1[i]|array2[i]  # bit or 연산자인 |를 이용해서 연산합을 한 새로운 num 구함
        
        while num > 1:  # num이 1이거나 0이 될 때까지 계속 수행한다
            if num%2 == 1:  # 2로 나눈 나머지가 1이면
                password[i] = '#' + password[i]  # 앞에 '#'을 추가한다
            else:  # 2로 나눈 나머지가 0이면
                password[i] = ' ' + password[i]  # 앞에 공백을 추가한다
            num //= 2

        if num == 1:  # 위의 while문으로는 마지막일 때 연산이 처리 되지 않기 때문에 마지막일때 수행하는 if 문을 추가한다
            password[i] = '#' + password[i]
        else:
            password[i] = ' ' + password[i]

        while len(password[i]) < N:  # 만약 제일 앞자리가 0이라면 앞에 공백이 포함되지 않기 때문에 자리수가 N이 될때까지
            password[i] = ' ' + password[i]  # 앞에 공백을 추가해준다

    print(password)