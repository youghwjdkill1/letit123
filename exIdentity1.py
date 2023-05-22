"""
파일명 : exIdentity1.py 
프로그램 설명 :  식별 연산자 예제 1
"""

# 파이썬에서는 모든 변수는 객체로 만든다.
# id() 함수: 변수의 메모리를 확인할 떄 사용한다.
a1 = 7
a2 = 7
a3 = 8
print(a1, a2, a3)
print("a1:", id(a1))   # 140711855252456
print("a2:", id(a2))   # 140711855252456
print("a3:", id(a3))   # 140711855252488
print(a1 is a2)        # True 
print(a1 is a3)        # False
print(a1 is not a3)    #True 동일한 객체가 아니므로


# 7. 식별 연산자 (Identity Operators)
# 두 변수가 동일한 객체인지 확인하는 연산자
# 결과: True, False

# 종류 : is, not is
# is : 두 객체가 같으면 True, 다르면 False  
# is not : 두 객체가 같지 않으면 True, 같으면 False

# 형식 : 
# a is b
# a is not b