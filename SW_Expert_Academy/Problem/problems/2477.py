import sys

sys.stdin = open('2477.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N, M, K, A, B = map(int,input().split())
    # N : 접수 창구 수, M : 정비 창구 수, K = 방문 고객 수
    # A : 지갑 두고 간 고객이 이용한 접수 창구 번호, B : 지갑 두고 간 고객이 이용한 정비 창구 번호
    a = list(map(int,input().split())) # N개
    b = list(map(int,input().split())) # M개
    t = list(map(int,input().split())) # K개

    reception = [False] * (N+1)
    repair = [False] * (K+1)
    reception_waiting = []
    repair_waiting = []

    customers = []
    time = 0; last = t[-1]+1
    customer_number = 1
    while time != last:
        customer_count = 0
        if time in t:
            customer_count = t.count(time)
        if customer_count:
            for _ in range(customer_count):
                customers.append([customer_number,0,0])
                t.pop(0); customer_number += 1

        for customer in customers:
            if customer[1] == 0:
                if sum(reception) == N:
                    reception_waiting.append(customer[0])
                else:
                    
        else:


        time += 1
        

    print(customers)