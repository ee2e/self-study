import sys

sys.stdin = open('4408.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]

    visited = []
    def DFS(data):
        cnt = 0
        for i in range(len(data)):
            if data[i] not in visited:
                visited.append(data[i])
            else:
                continue
            temp = [data[i]]
            for j in range(i+1,len(data)):
                for k in range(len(temp)):
                    if min(temp[k]) <= data[j][0] <= max(temp[k]) or min(temp[k]) <= data[j][1] <= max(temp[k]):
                        pass
                    else:
                        visited.append(data[j])
                        temp.append(data[j])
            cnt += 1
            if visited == data:
                break
        return cnt

    print(f'#{tc} {DFS(data)}')