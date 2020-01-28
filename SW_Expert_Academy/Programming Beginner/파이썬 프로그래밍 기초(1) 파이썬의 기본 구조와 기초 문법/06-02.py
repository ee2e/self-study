z = int(input())
p_num = []

for i in range(1,z+1) :
    if z % i == 0 :
        p_num.append(i)
        print(f'{i}(은)는 {z}의 약수입니다.')

if len(p_num) == 2 :
    print(f'{z}(은)는 1과 {z}로만 나눌 수 있는 소수입니다.')