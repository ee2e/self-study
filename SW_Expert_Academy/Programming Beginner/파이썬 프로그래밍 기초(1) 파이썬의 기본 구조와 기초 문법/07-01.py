scores = [88, 30, 61, 55, 95]

for idx, score in enumerate(scores, start = 1) :
    if score >= 60 :
        print(f'{idx}번 학생은 {score}점으로 합격입니다.')
    else :
        print(f'{idx}번 학생은 {score}점으로 불합격입니다.')