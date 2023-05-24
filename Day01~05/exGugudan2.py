"""
파일명: exGugudan2.py
프로그램 설명: while문을 이용한 구구단 출력하기
"""

# 초기값, 조건식, 실행문, 증감식 순으로 분석하기
# 2단 ~ 9단까지 출력
# 1. 바깥쪽 while문, 2. 안쪽 while문

dan = 2  # 1.초깃값

while dan <= 9:  # 1.조건식 2 ~ 9
    # 1.실행문
    i = 1  # 2.초깃값
    while i <= 9:  # 2.조건식 1 ~ 9
        print(f'{dan}x{i}={dan*i:<3d} ', end='')  # 2.실행문
        i += 1  # 2.증감식
    else:
        print()

    dan += 1  # 1.증감식