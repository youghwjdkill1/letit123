import getpass

userid = 'ghbc2024'
userpw = '2024'

inputuserid = input('아이디: ')
inputuserpw = getpass.getpass('비밀번호: ')

if userid == inputuserid and userpw == inputuserpw:
    print('로그인에 성공하셨습니다')
    print('ghbc2024님 환영합니다')
else:
    print('로그인에 실패하셨습니다')
    exit()