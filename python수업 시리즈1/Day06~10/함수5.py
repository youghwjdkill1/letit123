"""
파일명: 함수5.py
프로그램 설명: 함수의 유형
"""

def function():
    print('function() 실행!')

print(function(), type(function()))
if function() == None:
    print("^^")

# 첫 번째 유형
def f1(x):
    y = x + 5
    return y

number = f1(3)
print(number)

# 두 번째 유형
def f2():
    x = 3
    y = 5
    print(x+y)

f2()

# 세 번째 유형
def f3(x):
    y = 5
    print(x+y)

f3(3)

# 네 번째 유형
def f4():
    x = 3
    y = 5
    
    return x+y

print(f4())