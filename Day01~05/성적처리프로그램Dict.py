"""
파일명: 성적처리프로그램Dict.py
프로그램 설명: 이름,국어,영어,수학 점수를 입력을 받아서 처리하는 프로그램
"""

# student = { 'name':??, 'kor':??, 'eng':??, 'math':???, 'total':???, 'average': ?? }
student = {}  

# 1. 입력 부분
student['name'] = input('이름: ')
student['kor']  = int(input('국어점수: '))
student['eng']  = int(input('영어점수: '))
student['math'] = int(input('수학점수: '))
# print(student)

# 2. 처리 부분
student['total'] = student['kor'] + student['eng'] + student['math']
student['average'] = student['total'] / 3

# 3. 출력 부분
print(f'이름: {student["name"]}')
print(f'국어점수: {student["kor"]}')
print('영어점수: %d' %student['eng'])
print(f'수학점수: {student["math"]}')
print(f'총점: {student["total"]}')
print(f'평균: {student["average"]}')