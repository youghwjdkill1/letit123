"""
파일명: exContinue1.py
프로그램 설명: continue문
"""

#continue  #SyntaxError: 'continue' not properly in loop

i = 1
while i < 11:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
    i += 1
else:
    print('while문 종료')