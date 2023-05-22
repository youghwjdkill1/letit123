"""
파일명: 성적처리프로그램.py
프로그램 설명: 이름,국어,영어,수학 점수를 입력을 받아서 처리하는 프로그램
"""

# 1. 입력 부분
name = input('이름:이호정 ')
kor = int(input("국어점수: 12"))
eng  = int(input('영어점수: 7 '))
math = int(input('수학점수: 28 '))
# print(name, kor, eng, math)

# 2. 처리 부분
total = kor + eng + math
average = total / 3

# 3. 출력 부분
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {math}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')