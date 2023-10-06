""" 공 100미터 높이에서 떨어뜨리리고 높이 10 제기 """
# height = 100
# bounce = 3/5

# i = 1

# while i <= 10:
#     height = height * bounce
#     print(i, round(height,4))
#     i += 1

# 통과

""" 정수를 받고 한글로 내보내기 """
# number = int(input())

# if number == 1 :
#     print('일')
# elif number == 2 :
#     print('이')
# elif number == 3 :
#     print('삼')
# else:
#     print('1이상 3이하 정수만 입력해주세요.')

# 통과

""" 나이따른 세대 구분 """

# year = int(input())


# if 1900 < year > 1925 :
#     print('당신은 가장 위대한 새대에 태어났습니다.')
# elif 1924 < year > 1946 :
#     print('당신은 침묵 세대에 태어났습니다')
# elif 1945 < year > 1965 : 
#     print('당신은 베이비붐 세대에 태어났습니다')
# elif 1964 < year > 1981 : 
#     print('당신은 X세대에 태어났습니다.')
# elif 1980 < year > 1997 :
#     print('당신은 밀레니얼 세대에 태어났습니다.')
# elif 1996 < year > 2024 :
#     print('당신은 Z세대에 태어났습니다.')

# 애메하게 통과해버렸다.

""" 단위기호 """

# number = int(input())
# result = str(num)

# if num >= 1000:
#     result = str(num // 1000) + 'k'
# elif num >= 1000000 :
#     result = str(num // 1000000) +  'm'
# elif num >= 1000000000:
#     result = str(num // 1000000000) + 'K'
# elif num >= 1000000000000:
#     result = str(num // 1000000000000) + 'M'
# elif num >= 1000000000000000:
#     result = str(num // 1000000000000000) + 'G'
# elif num >= 1000000000000000000:
#     result = str(num // 1000000000000000000) + 'T'
# elif num >= 1000000000000000000000:
#     result = str(num //1000000000000000000000) + 'P'
# elif num >= 1000000000000000000000000:
#     result = str(num // 100000000000000000000000) + 'E'
# elif num >= 1000000000000000000000000000:
#     result = str(num // 100000000000000000000000000) + 'Z'   
# elif num >= 0 :
#     pass

# print(result)

# 통과

""" 제일 어렵고 내가 못했던 윤년 평년 판단하기 """

year = int(input())
leap_year = None


if year % 4 == 0 :
    if year % 100 == 0 :
        if year % 400 == 0 :
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False
    

if leap_year :
        print(year,'년은 윤년입니다.')
else :
    print(year,'년은 평년입니다.')  
# 비슷한데 while True 를 모르겠음  