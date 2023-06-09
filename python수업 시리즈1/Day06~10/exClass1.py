"""
파일명 : exClass1.py 
프로그램 설명 : 클래스 사용하기 (객체를 생성하지 않고 사용하기)
"""

# 1. 클래스 정의
class ClassTest1:
    a = 1  # 클래스 변수
    b = 2

    # 함수가 클래스 안으로 들어오면 method, 메서드(메소드)라고 불린다.
    def method1():
        """method1 정의"""
        print('method1()  실행!')
    
    def method2():
        """method2 정의"""
        print('method2() 실행!')


# 클래스 사용
# 파이썬에서는 클래스 자체를 사용할 수 있다.
# . 의 의미: ~의 라고 읽는다.
# 변수 사용 형식: 클래스명.변수명
# 함수 사용 형식: 클래스명.메소드(함수)명()

# 2. 클래스 변수 사용
# 형식: 클래스명.변수명
print(ClassTest1.a)  # 1
print(ClassTest1.b)  # 2

# 3. 클래스 메소드 사용
# 형식: 클래스명.메소드명()
ClassTest1.method1()
ClassTest1.method2()