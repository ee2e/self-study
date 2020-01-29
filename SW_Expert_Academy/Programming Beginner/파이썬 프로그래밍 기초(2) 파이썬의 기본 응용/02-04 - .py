'''
리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.

입력)
10
10
20
30
40

출력)
입력된 값 [10, 10, 20, 30, 40]의 평균은 22.0입니다.
'''

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

num_list = [num1,num2,num3,num4,num5]

print(f'입력된 값 {num_list}의 평균은 {sum(num_list) /len(num_list)}입니다.')