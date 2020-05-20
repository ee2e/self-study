A, B, V = map(int,input().split())

height = A; day = 1

while height < V:
    height += A - B
    day += 1

print(day)