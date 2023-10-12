""" 문제 """
# 미국과 달리, 우리나라에서는 보통 1995~1963년생을 '베이비붐 세대'로 봅니다.
# 사용자가 한국인인지에 따라 세대를 구분할 수 있게 프로그램을 고쳐 보세요.
# (문제를 단순화 하기 위해, 산업화 세대와 386세대느 고려하지 않습니다.)
# 그리고 사용자는 미국인 또는 한국인이라고 가정 합니다.

""" 예 """
# $ python3 generations2.py
# What year were you born? 1954
# Are you Korean?(y/n) y
# You're the Silent Generation.

# $ python3 generations2.py
# What year were you born? 1954
# Are you Korean?(y/n) n
# You're a baby boomer.

# 언제나 답은 150번 줄에 있습니다.

""" 나이에 따른 세대 구분 기본 코드 """
# year = int(input())

# if year <= 1924 :
#     print('가장 위대한 세대')
# elif year <= 1945 :
#     print('침목 세대')
# elif year <= 1964 :
#     print('베이비붐 세대')
# elif year <= 1980 :
#     print('X 세대')
# elif year <= 1996 :
#     print('밀레니엄 세대')
# elif year >= 1997 :
#     print('Z 세대')

""" 문제 풀어보는 곳 """

















































































































""" 정답 """
y = int(input('What year were you born? '))

gen = None
if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945 or (
        y <= 1954 and input("Are you Korean?(y/n) ").lower()[0] == 'y'
    ):
    gen = 'the Silent Generation'
elif y <= 1963 or (
        y <= 1964 and input("Are you Korean?(y/n) ").lower()[0] != 'y'
    ):
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")
