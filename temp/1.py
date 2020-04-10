import sys

sys.stdin = open('1.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    inputString = input()

    def solution(inputString):
        answer = -1
        left = ['(','{','[','<']
        right = [')','}',']','>']
        stack = []

        for string in inputString:
            if string in left:
                stack.append(string)
            elif string in right:
                if len(stack):
                    stack.pop()
                    answer += 1
                else:
                    return answer
        else:
            if answer == -1:
                return 0
            else:
                return answer + 1

    print(solution(inputString))