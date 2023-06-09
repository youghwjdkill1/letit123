# 1. 점수 입력
print('>>> 성적 처리 프로그램 <<<')
kor  = input('국어 점수: ')
eng  = input('영어 점수: ')
math = input('수학 점수: ')

# 2. 점수 체크
kor  = 0 if not kor.isdigit()  else int(kor)
eng  = 0 if not eng.isdigit()  else int(eng)
math = 0 if not math.isdigit() else int(math)

# 3. 점수 계산
total = kor + eng + math  # 총점
average = total / 3  # 평균

# 4. 학점 구하기
# A학점 : 90 ~ 100   , grade = 'A'
# B학점 : 80 ~ 89.9  , grade = 'B'
# C학점 : 70 ~ 79.9  , grade = 'C'
# D학점 : 60 ~ 69.9  , grade = 'D'
# F학점 : 0 ~ 59.9   , grade = 'F'
if average >= 90 and average <= 100:  # A학점 : 90 ~ 100
    grade = 'A'
elif average >= 80 and average < 90:  # B학점 : 80 ~ 89.9
    grade = 'B'
elif average >= 70 and average < 90:  # C학점 : 70 ~ 79.9
    grade = 'C'
elif average >= 60 and average < 70:  # D학점 : 60 ~ 69.9
    grade = 'D'
else:  # F학점 : 0 ~ 59.9  
    grade = 'F'

# 5. 점수 출력
print('>>> 점수의 결과 <<<\n'
     f'국어 점수: {kor}\n'
     f'영어 점수: {eng}\n'
     f'수학 점수: {math}\n'
     f'총점: {total}\n'
     f'평균: {average:.2f}\n'
     f'학점: {grade}')