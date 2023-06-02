"""
파일명: 함수9.py
프로그램 설명: 함수 예제
"""


# positional arguments : 
# 함수를 호출할 때 인수값을 순서대로 전달하는 방식
def f(a,b,c):
    print(a,b,c)

f(1,2,3)  # 1 2 3

# keyword arguments : 
# 함수를 호출할 때 인수값을 순서대로 저장하는 방식이 아니라 변수의 이름으로 값을 전달하는 방식
# 매개변수의 위치는 중요하지 않고 호출할 때 변수명만 맞추어주면 된다.
# 조건은 변수명이 동일해야 한다.
# 형식: 함수명(변수명=값)

# 순서에 상관이 없다.
f(a=1,b=2,c=3)  # 1 2 3
f(c=3,a=1,b=2)  # 1 2 3
f(b=2,c=3,a=1)  # 3 1 2 3

# positional 과 keyword arguments를 섞어서 사용하는 경우의 
# 대표적인 함수는 print() 함수이다.
# 주의할 점은 keyword arguments가 먼저오면 에러가 발생한다.
# https://docs.python.org/3/library/functions.html#print