""" 문제 """
# 정수를 한개 입력받아, 1부터 입력받은 수까지 각각에 대해 제곱을 구해 프리트 하는 프로그램을 작성해 보세요
# 단, while문을 사용하세요

''' 예 1 '''
# 입력 : 3
# 출력  
# 1 1
# 2 4
# 3 9

''' 예 2 '''
# 입력 : 5
# 출력
# 1 1
# 2 4
# 3 9
# 4 16
# 5 25

# 답은 언제나 150번 줄에
































































































































num = int(input())

i = 1

while i <= num:
    print(i, i * i)
    i = i + 1