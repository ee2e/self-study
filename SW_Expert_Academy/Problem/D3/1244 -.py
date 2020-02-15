import sys

sys.stdin = open('1244.txt', 'r')

T = int(input())

def my_max(args, start):
    result = 0
    idx = 0
    for i, v in enumerate(args):
        if i < start:
            continue
        if int(v) >= result:
            result = int(v)
            idx = i
    return idx

# def my_min(args):
#     result = 0x7ffffff
#     idx = 0
#     for i, v in enumerate(args):
#         if int(v) < result:
#             result = int(v)
#             idx = i
#     return idx

for tc in range(T):
    reward, time = input().split()
    time = int(time)
    reward = list(reward)

    start = 0
    for _ in range(time):
        max_idx = my_max(reward, start)
        for j in range(start, len(reward)):
            if reward[j] != max_idx:
                change = j
                break
        
        if max_idx > change:
            reward[max_idx], reward[change] = reward[change], reward[max_idx]
        
        start = change+1

    print(reward)