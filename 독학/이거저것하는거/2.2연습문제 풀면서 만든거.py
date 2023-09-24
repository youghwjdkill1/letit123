print('>>> 출생연도로 알아보는 자기 세대<<<')
i = 1
while i <= 3 :
    a = int(input('출생연도를 입력해주세요: '))
    
    if 1889 < a < 1924 :
        print('축하합니다. "가장 위대한 세대" 에서 태어나셨습니다.')
        i += 3
        break
    elif 1924 < a < 1946 :
        print('축하합니다. "침묵 세대" 에서 태어나셨습니다')
        i += 3
        break
    elif 1945 < a < 1965 :
        print('축하합니다. "베이비붐 세대" 에서 태어나셨습니다.')
        i += 3
        break
    elif 1964 < a < 1981 : 
        print('축하합니다. "X세대" 에서 태어나셨습니다.')
        i += 3
        break
    elif 1980 < a < 1997 :
        print('축하합니다. "밀리니얼 세대" 에서 태어나셨습니다.')
        i += 3
        break
    elif 1996 < a < 2003 :
        print('축하합니다. "Z세대" 에서 태어나셨습니다.')
        i += 3
        break
    elif 2003 < a < 2024 :
        print('축하합니다. "MZ세대" 에서 태어나셨습니다.')
        i += 3
        break
    else :
        print('이상한 출생연도를 입력하셨습니다.')
        i += 1
        print('실제 출생연도를 입력해주세요')
else : 
    print('출생연도를 3번이상 틀려 프로그램을 종료합니다')
    exit()

i = 1
print('>>> 자기가 태어난 세대가 좋다면 좋은 평점을 주세요! <<<')
while i <= 3 :
    a = int(input('5점만점중 몇점을 주고싶나요?'))

    if a == 0 :
        print('프로그램이 안좋으셨다면 죄송합니다.')
        print('다음에는 더 좋은 품질로 찻아오겠습니다.')
        i += 3
        exit()
    elif 0 < a < 3 :
        print('서비스가 살짝 별로 였나요?')
        print('혹시 별로여떤 점을 이메일로 보내주시면 감사하겠습니다')
        print('문의 이메일 : youghwjdkill2@gmail.com')
        i += 3
        exit()
    elif 2 < a < 4 :
        print('점수가 3점으로 중간이 이네요')
        print('다음에는 더 높은 점수를 받을수 있도록 노력 하겠습니다')
        i += 3
        exit()
    elif 3 < a < 5 :
        print('거의 만점을 주셨네요!')
        print('다음에는 5점을 받을수 있도록 노력하겠습니다.')
        i += 3
        exit()
    elif 4 < a < 6 :
        print('만점을 주셨네요!')
        print('프로그램에 만족하셨다니 다행이네요')
        i += 3
        break
    else :
        print('점수를 잘못입력하였습니다')
        print('점수는 1~5점만 줄수있습니다')
        print('점수를 계속 잘못 입력하면 프로그램이 종료됩니다!')
        i += 1
else :
    print('점수를 계속 잘못입력하여 프로그램을 종료 합니다.')
    exit()

print('점수를 5점을 주신 분깨만 드리는 특별한 혜택!')
print('회원가입을 하실수 있습니다')
i  = 1
print('>>> 회원가입을 원하시면 1번 아니면 2번을 눌러주세요 <<<')
while i <= 3 :
    a = int(input('숫자를 입력해주세요:'))

    if a == 1 :
        print('회원가입을 진행합니다')
        i += 3
        break
    elif a == 2 :
        print('회원가입을 진행하지 않습니다.')
        print('다음 만남을 기약하며 안녕히 들어가십쇼')
        exit()
    else :
        print('숫자를 잘못 입력하셨습니다')
        print('숫자를 3회이상 틀리면 프로그램이 종료 됩니다.')
        print('숫자를 다시 입력해주세요.')
        i += 1
else :
    print('숫자를 3회이상 틀려 프로그램을 종료합니다.')
    exit()

import getpass

userid = input('아이디를 입력해주세요: ')
userpw = input('비밀번호를 입력해주세요: ')
print('회원가입을 완료하엿습니다.')

print('>>> 로그인 <<<')
i = 0
while i < 3 :
    inputuserid = input('아이디를 입력해주세요: ')
    inputuserpw = input('비밀번호를 입력해주세요: ')

    if inputuserid == userid and userpw == inputuserpw :
        print('로그인 성공!')
        print(f'{userid}님 환영합니다')
        i += 3
        break
    else :
        print('아이디나 비밀번호가 틀렸습니다.')
        print('다시 입력해주세요.')
        print('3회이상 틀리면 프로그램이 종료됩니다')
        i += 1
else :
    print('아이디나 비밀번호를 3회이상 틀렸습니다.')
    print('프로그램을 종료합니다.')
    exit()

print('로그인 이후 컨테츠는 아직 비공개 입니다.')
print('다음에 이용해주세요. 감사합니다.')