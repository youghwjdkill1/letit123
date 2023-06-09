"""
파일명: jumsu1Function.py
프로그램 설명: 성적처리프로그램 
"""

def inputjumsu ():
    global name, kor , eng, math
    # 1. 입력 부분  
    name = input('이름: ')  
    kor  = int(input('국어점수: ')) 
    eng  = int(input('영어점수: ')) 
    math = int(input('수학점수: ')) 
    # print(name, kor, eng, math)   

def printjumsu():
    # 2. 처리 부분  
    total = kor + eng + math    
    average = total / 3 
        
    # 3. 출력 부분  
    print(f'이름: {name}')  
    print(f'국어점수: {kor}')   
    print(f'영어점수: {eng}')   
    print(f'수학점수: {math}')  
    print(f'총점: {total}') 
    print(f'평균: {average:.2f}')   
inputjumsu()