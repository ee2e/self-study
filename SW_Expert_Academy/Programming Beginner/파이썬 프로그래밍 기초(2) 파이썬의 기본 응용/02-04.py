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

num_list = []
num_list.append(int(input()))

print(f'입력된 값 {num_list}의 평균은 {sum(num_list) /len(num_list)}입니다.')