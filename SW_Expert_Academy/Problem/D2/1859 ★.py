import sys
sys.stdin = open('1859.txt','r')

T = int(input())

# def cal(args, result=0):
#     maximum = max(args)
#     idx = args.index(maximum)
#     if idx == 0:
#         return result
#     else:
#         for i in range(idx):
#             result += maximum - args[i]
#         for i in range(idx,0,-1):
#             args.remove(args[i])
#         return cal(args,result)
        
# for tc in range(T):
#     N = int(input())
#     daily = list(map(int,input().split()))

#     print(f'#{tc+1} {cal(daily)}')




# for tc in range(T):
#     N = int(input())
#     daily = list(map(int,input().split()))
#     result = 0
    
#     while len(daily) != 0:
#         maximum = max(daily)
#         idx = daily.index(maximum)
#         if idx == 0:
#             daily.pop(0)
#         else:
#             result += maximum*idx - sum(daily[:idx])
#             daily = daily[idx+1:]

#     print(f'#{tc+1} {result}')




for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    start = N-1
    result = 0
    for i in range(N-2,-1,-1):
        if data[start] < data[i]:
            start = i
        else:
            result += data[start]-data[i]
 
    print('#{} {}'.format(tc+1, result))