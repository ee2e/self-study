def solution(s):
    answer = []
    total = []
    s = s[1:]
    i = 0; num = ''
    while i < len(s):
        if s[i] == '{':
            i += 1; temp = []
            while s[i] != '}':
                while s[i].isdecimal():
                    num += s[i]
                    i += 1
                if num:
                    temp.append(int(num)); num = ''
                if s[i] == '}':
                    break
                i += 1
            total.append(temp)
        i += 1
        total.sort(key = len)

    for element in total:
        for i in range(len(element)):
            if element[i] in answer:
                pass
            else:
                answer.append(element[i])
                break     
    return answer