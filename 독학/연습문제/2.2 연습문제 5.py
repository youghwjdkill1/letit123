""" 연습문제: 윤년 판별하기 """
# 윤년은 역법을 실제 태양년에 맞추기 위해 여분의 하루 또는 월을 끼우는 해입니다.
# 현재 사용하는 그레고리력의 윤년 규칙은 다음과 같습니다.

''' 1. 서력 기원 연수가 4로 나누어 떨어지는 해는 윤년으로 한다. (1988년,1992년,1996년,
2004년,2008년,2012년,2016년,2020년,2024년2028년) '''
''' 2. 서력 기원 연수가 4,100으로 나누어 떨어지는 해는 평년으로 한다.
(1900년,2100년,2200년,2300년,2500년) '''
''' 3. 서력 기원 연수가 4,100,400 으로 나누어 떨어지는 해는 윤년으로 둔다.
(2000년, 2400년) '''

# 이 규칙에 따라, 연도를 나타내는 정수를 입력으로 받아서 윤년인지 아닌지
# 출력하는 프로그램을 작성해 보세요.

# 요번에도 답은 150번 줄에 있음요

""" 문제 풀어보는 곳 """




































































































































""" 정답 """
while True:
    is_leap_year = None

    year = int(input())

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year = True
    else:
        is_leap_year = False

    if is_leap_year:
        print(f'{year} is a leap year')
    else:
        print(f'{year} is not a leap year')

""" 내가 쓴거 """

# year = int(input())
# if year % 4 == 0 :
#     if year % 100 == 0:
#         if year % 400 == 0:
#             year = year

            
# if year % 100 == 0:
#     print(year,'년은 윤년입니다.')
# else : 
#     print(year,'년은 평년입니다.')