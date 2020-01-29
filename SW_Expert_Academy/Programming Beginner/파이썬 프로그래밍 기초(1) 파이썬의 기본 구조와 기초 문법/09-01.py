name = input()
age = int(input())

import datetime
dt = datetime.datetime.now()

a = 0
while age < 100:
    a += 1
    age += 1

print(f'{name}(은)는 {dt.year+a-1}년에 100세가 될 것입니다.')