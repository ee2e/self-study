# 다음과 같이 사용자 2명으로부터 가위, 바위, 보를 입력 받아
# 가위, 바위, 보 규칙이 정의된 함수를 이용해 승패를 결정하는 코드를 작성하십시오.

# 입력)
# 홍길동
# 이순신
# 가위
# 바위

# 출력)
# 바위가 이겼습니다!

user1 = input()
user2 = input()
rsp_1 = input()
rsp_2 = input()

def rsp(*args):
    if set(args) == {'가위', '바위'} :
        return "바위가 이겼습니다!"
    elif set(args) == {'가위', '보'} :
        return "가위가 이겼습니다!"
    elif set(args) == {'바위', '보'} :
        return "보가 이겼습니다!"
    else :
        return "비겼습니다!"

print(rsp(rsp_1, rsp_2))