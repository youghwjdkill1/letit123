""" 문제 """
# 다음 코드를 읽고, 실행 결과를 알아맞혀 보세요.

number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10 
    rev = rev * 10 + rem
    number = number // 10

print(rev)

""" 풀이 """
# 직접 실행해서 예사한 결곽가 나왔는지 확인해 보세요.
# 정답은 150번 줄에

""" 문제 풀어보기 """



































































































































""" 정답 해설 """
# number = 358                     # number 라는 변수를 지정 해준다

# rem = rev = 0                    # rem 이라는 변수와 rev라는 변수를 동시에 만들고 0 이라는 값을 준다
# while number >= 1:               # number 가 1보다 작아졌을때 while문을 종료한다라는 코드
#     rem = number % 10            # rem의 값은 number % 10 이기 떄문에 358 나누기 10에 나머지 값이다
#     rev = rev * 10 + rem         # rev의 값은 rev * 10 + rem의 값이기 떄문에 0 곱하기 10은 0 rem의 값은 8이기 떄문에 rev의 값은 8이된다
#     number = number // 10        # number에 값이 변하는 순간이다 number // 10이 새로운 number값이 된다. 358 나누기 10 하고 나머지를 없에면 number 값이 나온다

# print(rev) # 위에 있는 while문을 반복해서 거짓이 될때 까지 하고 while문을 탈출하고 나오면 마지막으로 바뀐 rev값은 프리트 하는것이기 떄문에 마지막dmfh 바뀐 rev값이 나온다
# 마지막 rec값이 정답이다 853이 정답이다