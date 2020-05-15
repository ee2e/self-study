import sys

input = sys.stdin.readline

hamber_minV = 2000
juice_minV = 2000

for i in range(5):
    x = int(input())
    if i < 3:
        if x < hamber_minV:
            hamber_minV = x
    else:
        if x < juice_minV:
            juice_minV = x

print(hamber_minV+juice_minV-50)