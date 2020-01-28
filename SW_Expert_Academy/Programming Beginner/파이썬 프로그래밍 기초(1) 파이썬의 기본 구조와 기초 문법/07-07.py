# 다음은 학생의 점수를 나타내는 리스트입니다.

# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.

# scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

# 출력)
# 454

i = 0
idx_list = []

while i < len(scores) :
    if scores[i] < 80 :
        idx_list.append(i)
    i += 1

idx_list_s = list(reversed(sorted(idx_list)))

j = 0
while j < len(idx_list_s) :
    scores.pop(idx_list_s[j])
    j += 1

print(sum(scores))