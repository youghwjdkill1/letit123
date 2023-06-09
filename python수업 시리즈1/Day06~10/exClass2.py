"""
파일명 : exClass2.py 
프로그램 설명 : 클래스 사용하기 (객체를 생성하고 사용하기)
"""
# 1. 클래스 정의
class ClassTest2:

    def method1(self):  # 인스턴스 메소드
        """method1() 정의"""
        self.a = 1  # 인스턴스 변수 (self ?)
        self.b = 2
    
    def printValue(self):
        """인스턴스 변수를 출력하는 메소드"""
        print(self.a, self.b)


# 2. 인스턴스(객체) 생성
# 형식: 변수명 = 클래스명()
ct2 = ClassTest2()  # 클래스가 그대로 메모리에 복사된다.

# 3. 인스턴스(객체) 사용
# 형식: 인스턴스.변수명
# 형식: 인스턴스.메소드명()
ct2.method1()
ct2.printValue()     # 1 2 
print(ct2.a, ct2.b)  # 1 2
