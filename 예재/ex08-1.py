while True:
    city = input('대한민국의 수도는 어디일까요?>>>')
    if city == '서울' or city == 'seoul' or city == 'SEOUL':
       print('정답입니다')
       break
    else:
        print('오답입니다 다시하세요!')
        