A, B, C = map(int,input().split())

sales = A//(C-B) if C > B else -2

print(sales+1)