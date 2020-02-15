import sys

sys.stdin = open('1228.txt', 'r')

for tc in range(10):
    original_length = int(input())
    original = list(map(int,input().split()))
    command_num = int(input())
    command = list(input().split())

    for i in range(len(command)):
        if command[i] == 'I':
            command[i] = 1
        
        command[i] = int(command[i])

    insert_num = 1
    while insert_num < len(command):

        for i in range(command[insert_num+1]):
            original.insert(command[insert_num]+i, command[insert_num+2+i])

        insert_num += 3 + command[insert_num+1]

    print(f'#{tc+1} {" ".join(map(str,original[0:10]))}')