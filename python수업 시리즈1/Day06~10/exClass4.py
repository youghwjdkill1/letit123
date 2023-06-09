"""
파일명 : exClass4.py 
프로그램 설명 : 생성자 사용하기 
"""

# 생성자는 인스턴스(객체)를 생성할 때 자동으로 호출되는 메소드다.
# 생성자의 역할은 값을 초기화할 때 사용한다.
# 생성자는 메소드명이 __init__ 이름으로 지정되어 있다.
class ClassTest4:

    def __init__(self, number1, number2, number3):
        """ 생성자 """
        print('생성자 메소드 실행!')
        self.number1 = number1
        self.number2 = number2
        self.number3 = number3
    
    def getNumber(self):
        print(self.number1, self.number2, self.number3)

ct41 = ClassTest4(1,2,3)
ct42 = ClassTest4(10,20,30)
ct43 = ClassTest4(100,200,300)
ct44 = ClassTest4(number3=100, number2=20, number1=1)
ct41.getNumber()  # 1 2 3
ct42.getNumber()  # 10 20 30
ct43.getNumber()  # 100 200 300
ct44.getNumber()  # 1 20 100