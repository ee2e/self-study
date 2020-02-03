import sys
sys.stdin = open('1288.txt','r')

T = int(input())

for tc in range(T):
    N = int(input())
    num_list = [0] * 10
    result = 0
    total = 0

    for i in range(7000):
        st = str(N)
        for s in st:
            num_list[int(s)] += 1
        result += 1

        for j in range(10):
            if not num_list[j] >= 1:
                break
            else:
                total = result

    print(total)