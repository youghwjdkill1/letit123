import getpass

userid = 'pythonuser'  # 단순변수 -> File -> DB
userpw = '123456'

print('>>> 로그인 <<<')
i = 1
while i <= 3:
    inputUserid = input('사용자: ')
    inputUserpw = getpass.getpass('비밀번호: ')

    if userid == inputUserid and userpw == inputUserpw:
        print('로그인 성공!')
        print(f'{userid}님 환영합니다.')
        i += 3
        break
    else:
        print('로그인 실패!')
        #exit()
        i += 1
        print('비밀번호가 틀렸습니다 다시 시도해주세요')  
else: 
    print('프로그램 종료') 
    exit()
print('로그인 성공후 파일코드를 불러옵니다')