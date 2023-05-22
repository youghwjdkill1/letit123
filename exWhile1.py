"""
파일명: exWhile1.py
프로그램 설명: while문
"""
# 반복문을 사용하지 않고 1 ~ 5까지 출력
i = 1
print(i)
i += 1
print(i)
i = 1
print(i)
i += 1
print(i)
i = 1
print(i)
i += 1
print(i)
i = 1
print(i)
i += 1
print(i)

i = 1         #초기값
while i <= 5: # 조건식
    print(i)  # 실행문
    i += 1    # 증감식
else:
    print('while문 종료')