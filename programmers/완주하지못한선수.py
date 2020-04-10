import sys

sys.stdin = open('완주하지못한선수.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    participant = list(input().split())
    completion = list(input().split())



    # # solved by eun
    # participant.sort()
    # completion.sort()

    # def solution(participant, completion):
    #     answer = ''
    #     for i in range(len(participant)):
    #         if i == len(completion) or participant[i] != completion[i]:
    #             answer += participant[i]
    #             break
    #     return answer




    # # 풀이 1)
    # import collections
    # def solution(participant, completion):
    #     print(collections.Counter(participant))
    #     print(collections.Counter(completion))
    #     answer = collections.Counter(participant) - collections.Counter(completion)
    #     print(answer)
    #     return list(answer.keys())[0]



    # 풀이 2)
    def solution(participant, completion):
        answer = ''
        temp = 0
        dic = {}
        for part in participant:
            dic[hash(part)] = part
            temp += int(hash(part))
        for com in completion:
            temp -= hash(com)
        answer = dic[temp]
        return answer



    result = solution(participant, completion)


    print(result)

