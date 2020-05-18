def self_number_check(num):
    global self_number
    result = num
    num = str(num)

    for n in num:
        result += int(n)
        if result > 10000:
            return

    if result <= 10000:
        self_number[result] = 1

self_number = [0]*10001

for i in range(1,10000):
    self_number_check(i)

for i in range(1,10001):
    if not self_number[i]:
        print(i)