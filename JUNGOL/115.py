m_list = list(map(int,input().split()))
k_list = list(map(int,input().split()))

if m_list[0] > k_list[0] and m_list[1] > k_list[1]:
    print(1)
else:
    print(0)