""" 문제 """

# 'input()'으로 사용자로부터 정수를 한개 입력받아, 그 숫자를 숫자 크기만큼 반복해서 출력하는 파이썬 스크립트를 작성하세요.
# 이때 출력 앞에 공백을 한칸 주어서, 입력과 출력이 구분되게 합니다.
# 단, 'while'문을 사용하세요

''' 예 1 '''
# 입력 : 3
# 출력 : 3 3 3

''' 예 2 '''
# 입력 : 5
# 출력 : 5 5 5 5 5

# 항상 그랬듯이 답은 150번 줄에






































































































































num = int(input())

i = 0
while i < num:
    print('', num)
    i += 1

# 해석
# num = int(input()) # 숫자를 입력할수 있게 해주는 명령어 이다

# i = 0              # i 는 변수인데 num에 들어간 값을 반복해서 내보내기 위해서 i라는 변수를 만들었다
# while i < num:     # while 반복문으로 들어가 i 가 num 보다 커질 때 까지 계속 반복 해준다
#     print('', num) # 한칸 비고 num에 들어간 수를 입력해준다
#     i +=  1         # i 에 수를 계속 추가해주는 명령어