"""
파일명 : exFile8.py
프로그램 설명 : 파일 입출력 예제 (텍스트 파일 복사)
"""

# 전용 함수를 사용하지 않고 원리를 알기 위한 코드
# 파일 복사의 개념
# 파일을 두개 열고
# 첫 번쨰 파일(원본 파일): 읽기 전용으로 연다.
# 두 번째 파일(복사본 파일): 쓰기 전용으로 연다.
# 원본 파일 에서 읽어서 복사본 파일로 쓰는 것이다.

# with문을 사용하지 않는 경
filename1 = 'data.txt'
filename2 = 'data.txt'

f1 = open(filename1, 'r', encoding='utf8')
f2 = open(filename2, 'w', encoding='utf8')

f2.write(f1.read())

f1.close
f2.close
# with문을 사용하는 경우
filename1 = 'data.txt'
filename2 = 'data.txt'

with open(filename1, 'r', encoding='utf8') as f1:
    with open(filename2, 'w', encoding='utf8') as f2:
        f2.write(f1.read())



