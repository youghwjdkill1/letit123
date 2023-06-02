value = 1

# 함수 내부에서 전역변수 읽기 
# 함수 내부에서 전역변수 value에 접근할 수 있다.
# r(읽기) 가능하다.
def printValue():
    print(value, type(value))

printValue()

# 함수 내부에서 전역변수 쓰기 
# 함수 내부에서 전역변수 value에 접근해서 저장한다.
# w(쓰기) 불가능하다.
def changeValue():
    value = 10
    print(value, type(value))

changeValue()
print(value)

# 함수 내부에서 전역변수 쓰기 
# 함수 내부에서 전역변수 value에 접근할 때 global 키워드를 사용하면
# 전역변수의 값을 변경할 수 있다. 
# 형식: global 변수명
# w(쓰기) 가능하다.
def changeValue2():
    global value
    value = 10
    print(value, type(value))

changeValue2()
print(value)   