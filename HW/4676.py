import sys

sys.stdin = open('4676.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    string = [x for x in input()]
    H = int(input())
    location = list(map(int,input().split()))

    location.sort(reverse=True)

    for i in location:
        string.insert(i,'-')
    
    print(f'#{tc}', "".join(string))