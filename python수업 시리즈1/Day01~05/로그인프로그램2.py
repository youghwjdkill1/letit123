userid = 'pythonuser'  # 단순변수 -> File -> DB
userpw = '123456'

print('>>> 로그인 <<<')
i = 1
count = 3
while i <= count:
    inputUserid = input('사용자: ')
    inputUserpw = input('비밀번호: ')

    if userid == inputUserid and userpw == inputUserpw:
        print('로그인 성공!')
        print(f'{userid}님 환영합니다.')
        break
    else:
        print('아이디 또는 비밀번호가 틀렸습니다.')
        i += 1
else:
    print("로그인 횟수를 초과하였습니다. 나중에 다시시도 해주세요")
    import sys
    sys.exit()  

print('다음코드를 출력합니다.')