"""
파일명 : exIfElse2.py
프로그램 설명 : if~else문을 로그인 프로그램

사용자명을 userid 변수에 저장한다.
비밀번호를 userpw 변수에 저장한다.
사용자에게 사용자명을 입력 받아서 inputUserid 변수에 저장한다.
사용자에게 비밀번호를 입력 받아서 inputUserpw 변수에 저장한다.

입력 받은 사용자 아이디와 userid 를 비교한다.
입력 받은 사용자 비밀번호와 userpw 를 비교한다.
두 값이 맞으면 로그인 환영 메세지를 출력 시키고 프로그램 실행으로 이동한다.
두 값이 틀리면 로그인 실패 메세지를 출력 시키고 프로그램을 종료한다.
"""
userid = 'pythonuse' #단순변수 -> File -> DB
userpw = '123456'

print('>>>로그인<<<')
inputuserid = input('사용자: ')
inputuserpw = input('비밀번호: ')

if userid == inputuserid and userpw == inputuserpw:
    print('로그인 성공')
    print(f'{userid}님 환영합니다')
else:
    print('로그인 실패!')
    exit()

print('로그인 후 실행되는 코드가 온다')