import sys

sys.stdin = open('다트게임.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    string = input()

    scores = [0]*3  # 각각의 기회에서 얻은 점수를 순서대로 넣는다
    score = 0
    i = j = 0
    while i < len(string):
        if string[i].isdecimal():  # string[i]가 점수인지 보너스인지 옵션인지 확인
            score = 0  # 보너스를 받기 전 점수를 저장 할 변수
            if string[i:i+2].isdecimal():  # 점수가 한자리 수인지 두자리 수인지 확인
                score = int(string[i:i+2])
                i += 2  # 점수가 두자리 수이면 인덱스에 2를 더해줌
            else:
                score = int(string[i])
                i += 1  # 점수가 한자리 수이면 인덱스에 1을 더해줌
        elif string[i].isalpha():
            if string[i] == 'D':  # 보너스가 'S'이면 1제곱을 해주는데 원래 수랑 같기 때문에 따로 확인하지 않는다
                score **= 2  # 보너스가 'D'일 때 2제곱
            elif string[i] == 'T':
                score **= 3  # 보너스가 'T'일 때 3제곱
            scores[j] += score  # 보너스 해준 값을 scores에 저장해준다
            i += 1; j += 1  # 인덱스도 1을 더해주고 기회도 다음으로 넘어간다
        else:  # 그러나 옵션이 있을 수가 있다
            if string[i] == '*':  # 스타상 당첨 시
                scores[j-1] *= 2  # 해당 점수를 2배해준다
                if j-2 >= 0:  # 만약 첫번째 기회가 아니라 두번째나 세번째 기회에 스타상을 받았을 경우
                    scores[j-2] *= 2  # 바로 전에 얻은 점수도 2배를 해 준다
            else:  # 아차상 당첨 시
                scores[j-1] *= (-1)  # 해당 점수는 마이너스가 된다
            i += 1  # 인덱스에 1을 더해줌

    print(sum(scores))