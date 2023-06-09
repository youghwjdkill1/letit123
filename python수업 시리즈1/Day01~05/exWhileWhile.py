"""
파일명: exWhileWhile.py
프로그램 설명: 중첩 while문(이중 while문)
"""
#첫 번쨰 while문 : 1 ~ 5까지 출력하는 코드
i = 1              # 초기값
while i <= 5:      # 조건식 i < 6, 5 >= i, 6 > i i = 4
    print(i)       # 실행문
    i += 1         # 증감식 i = 6

    # 두 번쨰 while문 : 6 ~ 10까지 출력하는 코드
    j = 6                  #초기값
    while j <= 10:         #조건식 j < 11, 10 >= k, 11 > j
        print(j)           #실행문
        j += 1             #증감식

        
        # 첫 번째 while문 : 1 ~ 5까지 출력하는 코드
i = 1          # 초기값
while i <= 5:  # 조건식 i < 6, 5 >= i, 6 > i
    print(i)   # 실행문
    i += 1     # 증감식

    # 두 번째 while문 : 6 ~ 10까지 출력하는 코드
    j = 6          # 초기값
    while j <= 10:  # 조건식 j < 11, 10 >= j, 11 > j
        print(j, end=' ')   # 실행문
        j += 1     # 증감식
    print()