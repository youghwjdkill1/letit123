"""
파일명: 함수7.py
프로그램 설명: 함수 예제
"""

# 매개변수에 *을 사용하면 나머지를 모두 묶는다.(자동으로 파이썬에서 처리한다.)
def function():
    print("function() 함수 실행!")
    return 1,2,3,4,5

a,b,*c = function()
print(a,b,c) # 1 2 [3, 4, 5]

a,*b,c = function()
print(a,b,c) # 1 [2, 3, 4] 5

*a,b,c = function()
print(a,b,c) # [1, 2, 3] 4 5