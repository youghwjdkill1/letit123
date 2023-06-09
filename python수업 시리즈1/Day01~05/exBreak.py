"""
파일명 : exBreak.py
프로그램 설명 : break문
"""

#break  #syntaxError: 'break' outside loop
i = 1           #초기값
while i <= 5:   #조건식
    print(i)    #실행문
    i += 1      #증감식
    if i == 3:
        break

print('프로세서 종료')
print()

i = 1
while i <= 10:
    if i % 2 == 0:
        print(1)
        if i == 4:
            break
    i += 1

print('프로세서 종료')