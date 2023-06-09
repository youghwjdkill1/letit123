"""
파일명 : jumsu1Class.py
프로그램 설명 : 성적처리 프로그램을 클래스로 변경 (클래스로 변경한 소스코드)
"""


# 1. 클래스 정의
class Jumsu:

    def inputJumsu(self):
        # 1. 점수 입력
        print('>>> 성적 처리 프로그램 <<<')
        self.kor  = input('국어 점수: ')
        self.eng  = input('영어 점수: ')
        self.math = input('수학 점수: ')

        # 2. 점수 체크
        self.kor  = 0 if not self.kor.isdigit()  else int(self.kor)
        self.eng  = 0 if not self.eng.isdigit()  else int(self.eng)
        self.math = 0 if not self.math.isdigit() else int(self.math)
	# jumsu1.getGrade(), jumsu2.getGrade()로 사용하면 안되고 self를 사용해야 한다.
        self.getGrade()  

    def getGrade(self):
        # 3. 점수 계산
        self.total = self.kor + self.eng + self.math  # 총점
        self.average = self.total / 3  # 평균

        # 4. 학점 구하기
        # A학점 : 90 ~ 100   , grade = 'A'
        # B학점 : 80 ~ 89.9  , grade = 'B'
        # C학점 : 70 ~ 79.9  , grade = 'C'
        # D학점 : 60 ~ 69.9  , grade = 'D'
        # F학점 : 0 ~ 59.9   , grade = 'F'
        if self.average >= 90 and self.average <= 100:  # A학점 : 90 ~ 100
            self.grade = 'A'
        elif self.average >= 80 and self.average < 90:  # B학점 : 80 ~ 89.9
            self.grade = 'B'
        elif self.average >= 70 and self.average < 90:  # C학점 : 70 ~ 79.9
            self.grade = 'C'
        elif self.average >= 60 and self.average < 70:  # D학점 : 60 ~ 69.9
            self.grade = 'D'
        else:  # F학점 : 0 ~ 59.9  
            self.grade = 'F'
        self.printJumsu()

    def printJumsu(self):
        # 5. 점수 출력
        print('>>> 점수의 결과 <<<\n'
            f'국어 점수: {self.kor}\n'
            f'영어 점수: {self.eng}\n'
            f'수학 점수: {self.math}\n'
            f'총점: {self.total}\n'
            f'평균: {self.average:.2f}\n'
            f'학점: {self.grade}')

# 2. 인스턴스(객체) 생성
jumsu1 = Jumsu()
jumsu2 = Jumsu()

# 3. 인스턴스 메소드 실행
jumsu1.inputJumsu()
jumsu2.inputJumsu()