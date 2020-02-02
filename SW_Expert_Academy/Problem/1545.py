'''
주어진 숫자부터 0까지 순서대로 찍어보세요

입력)
8
출력)
8 7 6 5 4 3 2 1 0
'''

num = int(input())
num_list = []
for i in range(num,-1,-1):
    num_list.append(i)
print(' '.join(map(str,num_list)))