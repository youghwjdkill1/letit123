"""
파일명 : exClass3.py 
프로그램 설명 : 디버깅을 이용한 클래스/인스턴스 주소 확인하기
"""

# 1. 클래스 정의
class ClassTest3:

    # 인스턴스가 생성되지 않았기 때문에 에러가 발생된다.
    # self.a = 1
    a = 1
    b = 2

    def func1(self):
        """func1() 메소드 정의"""
        print("func1() 메소드 실행!")

    def printSelf(self):
        """self의 주소를 출력하는 메소드"""
        print('printSelf() 메소드 실행!')
        print(self)
        print(id(self))
        print(hex(id(self)))

# 2. 인스턴스(객체) 생성
# 형식: 객체변수명 = 클래스명()  <-- 함수 호출하듯이 사용한다.
ct3 = ClassTest3()

print(ct3)          # 주소 출력(16진수) 0~9abcdef 10~19 1a 1b 1c 1d 1e 1f 20
print(id(ct3))      # 주소 출력(10진수) 
print(hex(id(ct3))) # 주소 출력(16진수)
ct3.printSelf()     # self의 주소가 출력

# 3. 인스턴스(객체) 메소드 사용
# 형식: 인스턴스명(객체).메소드명(), 인스턴스명(객체).변수명
# . 의미: ~ 의라고 읽는다.
# . 의미: ~에 존재하는 이라고 읽는다.

# ct3의 func1() 메소드 실행
ct3.func1()  # ct3에 존재하는 func1()을 호출한다. 
print(ct3.a,ct3.b)  # 1 2 