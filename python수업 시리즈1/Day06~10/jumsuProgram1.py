"""
파일명: jumsuProgram1.py
프로그램 설명: 점수 관리 프로그램
작성자: 파이썬마스터
"""

import os

filename = 'jumsuProgram1.txt'

def jumsuAdd():
    """점수 추가"""

    # 1. 점수 입력
    print("점수를 입력하세요.")
    name = input("이름: ")
    kor  = input("국어 점수 : ")
    eng  = input("영어 점수 : ")
    math = input("수학 점수 : ")

    # 2. 점수 체크
    kor  = int(kor)  if kor.isdigit()  else 0
    eng  = int(eng)  if eng.isdigit()  else 0
    math = int(math) if math.isdigit() else 0

    # 3. 점수 계산
    total = kor + eng + math  # 총점 
    #total = sum([kor, eng, math])  # 총점  
    average = total / 3  # 평균 

    # 4. 점수 출력
    print("\n>>> 점수의 결과 <<<\n"
        f"이름 : {name}\n"
        f"국어 점수 : {kor}\n"
        f"영어 점수 : {eng}\n"
        f"수학 점수 : {math}\n"
        f"총점 : {total}\n"
        f"평균 : {average:.2f}\n"
        ">>> 점수의 결과 <<<")

    # 5. 파일 저장
    with open(filename, 'a', encoding='utf8') as f:
        f.write(">>> 점수의 결과 <<<\n"
            f"이름 : {name}\n"
            f"국어 점수 : {kor}\n"
            f"영어 점수 : {eng}\n"
            f"수학 점수 : {math}\n"
            f"총점 : {total}\n"
            f"평균 : {average:.2f}\n"
            ">>> 점수의 결과 <<<\n\n")

    print(f'{filename} 파일로 점수를 저장했습니다.')
    print('엔터키를 누르세요...')
    input()

def jumsuView():
    """점수 확인"""
    
    # 점수 파일 읽기
    with open(filename, 'r', encoding='utf8') as f:
        print(f.read())
        
    print('엔터키를 누르세요...')
    input()

def jumsuMenu():
    """메뉴"""
    menu  = '>>> 점수 관리 프로그램 <<<\n'
    menu += '1. 점수 추가\n'
    menu += '2. 점수 확인\n'
    menu += 'q. 프로그램 종료'
    
    print(menu)

def main():
    """main 함수"""

    while True:

        os.system('cls')  # 화면 지우기

        jumsuMenu()
        x = input('선택 >>> ')  # 메뉴 입력

        # 메뉴 체크
        if   x == '1' :
            jumsuAdd()
        elif x == '2' :
            jumsuView()
        elif x == 'q' : 
            break
        else:
            print('1, 2, q 중에서 입력하세요.')
            os.system('pause')

main()

print('점수 관리 프로그램을 종료합니다.')