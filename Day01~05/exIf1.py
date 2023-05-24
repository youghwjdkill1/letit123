"""
파일명: exIf1.py
프로그램 설명: 단일 if문
"""
# 단일 if문
# 참일 때만 실행하는 구조이다.
# 거짓일 떄는 실행하는 부분이 없다.
a = 2
b = 8

# 관계 연산자
# 형식:
# if a 관계 연산자 b:
#     실행문
# 

if(a == 2):
    print('이 부분이 실행됩니다')

if not a > 10:
    print('a는 10보다 큽니다.')

if a:
    print('참이므로 실행됩니다.')



# #########
# ## 제어문 
# #########

# 제어문이란 프로그램의 실행 흐름을 제어할 때 사용한다.
# 종류 : if, while, for, break, continue

# 조건문
# 조건문이란 실행문을 조건을 판단해서 실행하는 제어문으로 if문이 여기에 해당된다.

# 반복문
# 반복문이란 실행문을 반복해서 실행할 때 사용하는 제어문으로 while, for문이 여기에 해당된다.

# if문
# if문은 조건문으로 프로그램의 흐름을 제어할 때 사용하는 제어문이다.

# 예를 들어서 

# 우산을 챙긴다.
# 구두를 신는다.
# 외출한다.


# if 밖에 비가오는가 ?:
#     우산을 챙긴다.
#     구두를 신는다.
# else:
#     운동화를 신는다.

# 외출한다.


# if문은 4가지 종류가 있다.
# 단일 if문, if~else문, 다중if문, 중첩if문
# 단일 if문 형식 : 
# if 조건식 : <-- 조건식은 참(True)과 거짓(False)을 판단할 수 있어야 한다.
#     실행문  <-- 조건식이 참이면 실행문이 실행된다.
#       :

# if ~ else 문 :
# if 조건식 :
#     실행문1  <-- 조건식이 참이면 실행문1이 실행된다.
#        :
# else:
#     실행문2  <-- 조건식이 거짓이면 실행문2가 실행된다.
#        :

# 다중 if문 형식 :
# if 조건식1 :
#     실행문1   <-- 조건식1이 참이면 실행문1이 실행된다.
#       :
# elif 조건식2: <-- 조건식1이 거짓이면 조건식2를 실행한다. 
#     실행문2   <-- 조건식2가 참이면 실행문2가 실행된다.
#       :     
# elif 조건식3: <-- 조건식2가 거짓이면 조건식3을 실행한다. 
#     실행문3   <-- 조건식3이 참이면 실행문3이 실행된다.
#       :
# elif 조건식4: <-- 조건식3이 거짓이면 조건식4를 실행한다. 
#     실행문4   <-- 조건식4가 참이면 실행문4가 실행된다.
#       :
# else:         <-- 조건식4가 거짓이면 이 부분이 실행한다.  (생략 가능)
#     실행문5   <-- 조건식4가 기짓이면 실행문5가 실행된다.
#       :

# 중첩 if문
# if 조건식 :
#     실행문  <-- 조건식이 참이면 실행문이 실행된다.
#       :     
#     if 조건식 :
#         실행문
#           :


# 자료형의 참과 거짓의 판단 기준
#         True           False
# 숫자     1(0이 아닌 숫자)  0          
# 문자열   "test"           ""   <-- 값이 있으면 참, 없으면 거짓
# 리스트   [1,2,3]          []   <-- 값이 있으면 참, 없으면 거짓
# 튜플     (1,2,3)          ()   <-- 값이 있으면 참, 없으면 거짓
# 딕셔너리 {"a" : "b"}      {}   <-- 값이 있으면 참, 없으면 거짓
# 불리언   True            False

# if dictData :
#     :

# if listData :
#     :

# 관계 연산자(비교 연산자)의 판단 기준
# x = 3
# y = 2

# x > y    x가 y보다 크다
# x < y    x가 y보다 작다
# x >= y   x가 y보다 크거나 같다
# x <= y   x가 y보다 작거나 같다
# x == y   x와 y가 같다
# x != y   x와 y가 같지 않다


# if x > y :
#    :
# if x == y :
#    :

# 논리 연산자의 판단 기준
# x = 3
# y = 2

# a : x == 3 
# b : y != 2
# a or b   a와 b 둘 중에 하나만 참이면 참
# a and b  a와 b둘 다 참이어야 참
# not a    a가 거짓이면 참

# if x != y and x >= 3:
#   :

# if not x:
#   :

# 멤버쉽 연산자
# a = [1,2,3,4,5]
# if 1 in a :
#   :

# 식별연산자
# if a is b :
#   :

# X
# if a = 1:
#    :