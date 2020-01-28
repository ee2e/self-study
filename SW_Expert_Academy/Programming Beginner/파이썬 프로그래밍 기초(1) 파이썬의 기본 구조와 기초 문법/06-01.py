z = int(input())

for i in range(1,z+1) :
    if z % i == 0 :
        print(f'{i}(은)는 {z}의 약수입니다.')