import sys

sys.stdin = open('1230.txt', 'r')

for tc in range(10):
    original_length = int(input())
    original = list(map(int,input().split()))
    command_num = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            command[i] = 1
        elif command[i] == 'D':
            command[i] = 2
        elif command[i] == 'A':
            command[i] = 3
        
        command[i] = int(command[i])

    insert_num = 1
    while insert_num < len(command):

        if command[insert_num-1] == 1:
            for i in range(command[insert_num+1]):
                original.insert(command[insert_num]+i, command[insert_num+2+i])
            insert_num += 3 + command[insert_num+1]
        elif command[insert_num-1] == 2:
            for _ in range(command[insert_num+1]):
                original.pop(command[insert_num])
            insert_num += 3
        elif command[insert_num-1] == 3:
            for i in range(command[insert_num]):
                original.append(command[insert_num+1+i])
            insert_num += 2 + command[insert_num]

    print(f'#{tc+1} {" ".join(map(str,original[0:10]))}')