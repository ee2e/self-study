def remove(data):
    data = list(set(data))
    return data

result = remove([12,24,35,24,88,120,155,88,120,155])

print(result)
