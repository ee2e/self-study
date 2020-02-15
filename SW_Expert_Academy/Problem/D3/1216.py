import sys

sys.stdin = open('1216.txt', 'r')

for tc in range(10):
    n = int(input())
    matrix = [[x for x in input()] for _ in range(100)]

    s1 = ''
    s2 = ''
    maximum = 0
    
    for i in range(100):

        for k in range(100):
            s1 += matrix[i][0+k]
            s2 += matrix[0+k][i]

        for k in range(100,0,-1):
            ss1 = s1[:k]
            ss2 = s2[:k]
            ss3 = s1[100-k:]
            ss4 = s2[100-k:]

            for l in range(k,-1,-1):
                sss1 = ss1[:l]
                sss2 = ss2[:l]
                sss3 = ss1[k-l:]
                sss4 = ss2[k-l:]

                if sss1 == sss1[::-1]:
                    if len(sss1) > maximum:
                        maximum = len(sss1)

                if sss2 == sss2[::-1]:
                    if len(sss2) > maximum:
                        maximum = len(sss2)
                
                if sss3 == sss3[::-1]:
                    if len(sss3) > maximum:
                        maximum = len(sss3)

                if sss4 == sss4[::-1]:
                    if len(sss2) > maximum:
                        maximum = len(sss3)

                if maximum > len(sss1):
                    break
            
            if maximum > len(ss1):
                break

        s1 = ''
        s2 = ''

    print(f'#{n} {maximum}')