A, B = input().split()

for i in range(2,-1,-1):
    if A[i] > B[i]:
        result = A[::-1]
        break
    elif A[i] < B[i]:
        result = B[::-1]
        break

print(result)