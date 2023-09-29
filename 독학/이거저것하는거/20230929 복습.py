""" 윤년판단하기 연습문제를 바로 풀어보기 """

# year = int(input())

# if year % 4 == 0: 
#     False
#     if year % 100 == 0:
#         False
#         if year % 400 == 0: 
#             False
#         else: 
#             True
#     else:
#         True
# else:
#     True

# if False:
#     print(year,'년은 평년입니다')
# else:
#     print(year,'년은 윤년입니다.')


""" 실패 """

""" 받아적기 """


while True:
    year = int(input())
    
    is_leap_year = None
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        else:
            is_leap_year =  True
    else:
        is_leap_year = False

    if is_leap_year :
        print(year,'년은 윤년입니다')
    else:
        print(year,'년은 평년입니다.')
break