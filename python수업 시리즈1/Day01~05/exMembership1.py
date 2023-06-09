"""
파일명: exMembership1.py 
프로그램 설명:  멤버쉽 연산자 예제 1
"""

# 리스트 변수 number에 1 ~ 5까지 저장한다
number = [1, 2, 3, 4, 5]

# 반복이 가능한지 확인한다.
print(iter([]), iter(number))

# number 변수에 5가 존재합니까 ?
print(5 in number)   #True
# number 변수에 13이 존재합니까 ?
print(13 in number)  #True
print()

a = 1
print(a == 1 or a == 2 or a == 3)   # True
print(a in (1,2,3,))                # True

# 6. 구성원 연산자 (Membership Operators)
# 구성원의 존재 유무를 확인하는 연산자
# 값이 있는지 없는지 판단할 때 사용한다.
# 결과: True, False

# 종류 : in, not in
# in     : 값이 존재하면 True, 존재하지 않으면 False
# not in : 값이 존재하지 않으면 True, 존재하면 False
# 형식 : 
# a in b  <-- 반드시 b는 반복할 수 있는 iterable 이 와야 한다. (문자열,리스트,튜플,딕셔너리,셋)
# a not in b
 