# 소수를 검사하는 함수를 정의하고, 다음의 결과와 같이 사용자가 입력한 숫자가
# 소수인지를 판단하는 프로그램을 작성하십시오.
# 소수일 경우 "소수입니다." 출력, 아닐 경우 "소수가 아닙니다." 출력

# 입력)
# 13

# 출력)
# 소수입니다.

num = int(input())

def pri(n):
    div_list = []
    for i in range(n,0,-1):
        if n % i == 0:
            div_list.append(n)
    if len(div_list) == 2:

        return "소수입니다."
    else:
        return "소수가 아닙니다."

print(pri(num))