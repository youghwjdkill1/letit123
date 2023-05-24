import getpass

userid = 'ghbc2023'
userpw = '2023'

inputuserid = input('아이디: ')
inputuserpw = getpass.getpass('비밀번호: ')

if userid == inputuserid and userpw == inputuserpw:
    print('로그인을 성공하셨습니다')
    print('ghbc2023님 환연합니다!')
    print('다음코드 파일을 불러옵니다')
else:
    print('로그인에 실패하셨습니다')
    exit()