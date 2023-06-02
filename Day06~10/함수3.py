"""
파일명 : 함수3.py
프로그램 설명 : 함수 예제
"""

# 함수를 이용해서 2단을 출력한 경우

def gugudan():
#     dan = 2
#     for i in range(1,10):
#         print(f'{dan}x{i}={dan*i}', end='  ')
#     else:
#         print()

# gugudan()     


def gugudan(dan):
    for i in range(1,10):
        print(f'{dan}x{i}={dan*i:<2d}', end='  ')
    else:
        print()

# gugudan(2)
# gugudan(3)
#   :
# gugudan(7)
# gugudan(8)
# gugudan(9)

# 2단 ~ 9단까지 효율적으로 호출하는 방법은?
for i in range(2,10):
    gugudan(i)