""" 연습문제: 단위 기호 """
# 길이,부피,무게나 금액을 표기할 때 100을 'k'로 표기하곤 합니다.
# 예를 들어, 3000m는 3km로 표기하는것이 일방적입니다.

# 다음은 입력받은 숫자가 1000보다 크면 1자리부터 100자리까지의 숫자를 생약하고 'k'를 붙여주는 파이썬 코드입니다.

# num = int(input())
# result = str(num)

# if num >= 1000:
#     result = str(num // 1000) + 'k'
# elif num >= 0:
#     pass

# print(result)

# 코드 설명:
# 1번쨰 줄: 입력받은 문자열을 정수(int)로 바꿧습니다. 나중에 숫자끼리 비교할때 쓰려고 그렇게 한겁입니다.
# 2번째 줄: if 문의 계산 결과를 담을 변수를 result라는 이름으로 만들었습니다.
# 4~5번째 줄 : 숫자가 1000이상인지 검사해서 결과값(result)을 만듭니다.
# 1 ~ 100 자리 숫자를 생략하려고 정수의 나눗셈(//)을 이용했습니다.
# 6~7번째 줄: 숫자가 (1000보다 작고) 0 이상이면 아무 일도 하지 않았습니다(pass).
# 9번째 줄: result를 출력합니다.

""" 문제 """
# 1. 백만 이상의 숫자를 입력받았을 때 1 ~ 10만자리 숫자를 생략하고 'M'을 붙여서 풀력하게 코드를 수정해 보세요.
# 예시
# >python affix .py 
# 1000000
# 1M

# 2. 1번을 성공했다면, 그 이상도 구현해 보세요(10의 승수 단위 참조).

# 답은 언제나 150번 줄에

""" 문제 풀어보는 곳 """

















































































































""" 정답 """
num = int(input())
result = str(num)
    
if num >= 1000000000000000000:
    result = str(num // 1000000000000000000) + 'E'
elif num >= 1000000000000000:
    result = str(num // 1000000000000000) + 'P'
elif num >= 1000000000000:
    result = str(num // 1000000000000) + 'T'
elif num >= 1000000000:
    result = str(num // 1000000000) + 'G'
elif num >= 1000000:
    result = str(num // 1000000) + 'M'
elif num >= 1000:
    result = str(num // 1000) + 'k'
elif num >= 0:
    pass
    
print(result)

""" 내가 한거 """
# num = int(input())
# result = str(num)

# if 999999 > num >= 1000:
#     result = str(num // 1000) + 'K'
# elif 999999999 > num >= 1000000 :
#     result = str(num // 1000000) + 'M'
# elif 999999999999 > num >= 1000000000 :
#     result = str(num // 1000000000) + 'G'
# elif num >= 1000000000000 :
#     result = str(num // 1000000000000) + 'T'
# elif num >= 0:
#     pass

# print(result)

# 이거 만든 새끼도 대단하다 0을 어덯게 다 계산한거야 ㅁㅊ