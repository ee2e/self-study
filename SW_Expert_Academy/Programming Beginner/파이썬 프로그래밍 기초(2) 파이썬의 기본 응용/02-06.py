'''
다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.

입력)
12

출력)
[1, 2, 3, 4, 6, 12]
'''

num = int(input())
div = []

for i in range(num,0,-1):
    if num % i == 0:
        div.append(i)

div.sort()

print(div)