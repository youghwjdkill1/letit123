# 1.로그인 가능
import getpass

userid = 'pythonuser'  # 단순변수 -> File -> DB
userpw = '123456'

print('>>> 로그인 <<<')
inputUserid = input('사용자: ')
inputUserpw = getpass.getpass('비밀번호: ')

if userid == inputUserid and userpw == inputUserpw:
    print('로그인 성공!')
    print(f'{userid}님 환영합니다.')
else:
    print('로그인 실패!')
    exit()
# 2. 입력 부분
name = input('이름: ')
kor = int(input("국어점수: "))
eng  = int(input('영어점수:'))
math = int(input('수학점수: '))
# print(name, kor, eng, math)

# 3. 처리 부분
total = kor + eng + math
average = total / 3

# 4. 출력 부분
print(f'이름: {name}')
print(f'국어점수: {kor}')
print(f'영어점수: {eng}')
print(f'수학점수: {math}')
print(f'총점: {total}')
print(f'평균: {average:.2f}')