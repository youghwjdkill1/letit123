# 결과 값을 구하시오

# number = 106

# rem = rev = 0

# while number > 1 :
#     rem = rev + number
#     rev = number
#     number = number // 10

# print(rem)

# while문을 처음 시작할때 변수들에 수들 rem = 106 , rev = 106, number = 10     
# while문을 두번째로 시작할때 변수들에 수들 rem = 116  rev = 10 number = 1    
# while문을 세번째로 시작할때 변숟에 수들 rem = 116
# print(rem) 출력하는 수는 116 이다

# 위에 결과가 나오려면 while number >= 1 : 이 아니라 while number > 1: 이렇게 되어야지 맞는거다
# 만약 while number >= 1 : 이렇게 써번리면 1이 number이 1이 되었을때 같기 떄문에 참이라는 결과가 나와 while문을 한번 더 진입한다
# 항상 주의 하면서 잘 보고 안하면 아예 다른 결과가 나오기 때문에 조심해야하는 부분인건같다 

""" 연습문제 3번 풀기 """

# ball = 100
# bounce = 3/5

# i = 1

# while i <= 10 :
#     ball = ball * bounce
#     print(i, round(ball,4))
#     i = i + 1

# 정확하게 기억하고 풀이를 할수있는거 같다. 정답이다