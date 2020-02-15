import sys

sys.stdin = open('graph_path.txt', 'r')

T = int(input())

def CRTESTACK(): return []
def PUSH(stack,c): return stack.append(c)
def POP(stack): return stack.pop(-1) if len(stack) else None
def PEEK(stack): return stack[-1] if len(stack) else None
def ISEMPTY(stack): return len(stack) == 0

def DFS(graph,v,stack,visited):
    global G
    if v in graph.keys():
        for n in graph[v]:
            if n not in visited:
                PUSH(stack,n)
    if v not in visited:
        visited.append(v)
    v = POP(stack)
    return visited if v == None else DFS(data,v,stack,visited)

for tc in range(T):
    V, E = map(int,input().split())

    data = {}
    for _ in range(E):
        node1, node2 = map(int,input().split())
        if node1 not in data.keys():
            data[node1] = [node2]
        else:
            data[node1] += [node2]

    S, G = map(int,input().split())
    stack = CRTESTACK()
    visited = []
    DFS(data,S,stack,visited)

    if G in visited:
        result = 1
    else:
        result = 0

    print(f'#{tc+1} {result}')
