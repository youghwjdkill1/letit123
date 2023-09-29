""" and/or 연산자 """
# 이번에는 조건문에서 많이 쓰이는 'and'와'or' 연산자를 알아볼게요.

""" if 문에 and/or 를 사용 """
# 'if'문에 'and','of'를 사용할 수 있습니다.
# 예를 들어 보겠습니다. 다음과 같이 문자열's'가 있다고 할때,
'''
s = 'banana'
''' 
# 다음과 같이 중첩된 if문은,
''' 
if 'a' in s :   
        if 'b' in 'banana':
            print('banana에는 a 도 있고 b도 있어요')
'''
# 'and'를 써서 다음과 같이 바꿀 수 있습니다.
'''
if 'a' in s and 'b' in s:
    print('banana에는 a도 있고 b도 있어요!')
'''
# 중첩되었도 if문을 if 한 번으로 줄였습니다.

# 여기서 퀴즈!

# and 대신 or를 써서, 'bananan에는 a 또는 c가 있어요!'라고 출력하는 문자을 만들어 보세요
""" 여기다가 만들어 보세요! """
"""
if 'a' in 'banana' or 'b' in 'bananan' :
    print('banana 안에 a 와 b가 있어요')
"""

""" if문 없이 and/or만 사용 """
# 사실, and와 or는 반드시 if문에 들어가야만 하는 것은 아니고, 다음과 같이 and또는 or를 단독으로 사용해도 됩답니다.
'''
'a' in s  # True
'b' in s  # True
'c' in s  # False
'''
# 이러한 True/False 값을 불(bool)이라고 하는데
# 불값을 변수에 넣을수도 있습니다.
'''
a_in_s = 'a' in s
a_in_s    # True
'''

""" and/or 연산 순서 """
# 파이썬에서는 and/or의 왼쪽 항을 먼저 평가(계산)하고, 오른쪽 항은 필요할 떄만 평가합니다
# 그리고 대부분 고급 언어에서 이렇게 합니다

# 예를 들어볼게요.
# a 와 b 값이 다음과 같을 때,
'''
a = 3
b = 0
'''
# b 값이 0이므로  b를 분모로 하여 나눗셈을 하면 다음과 같이
# ZeroDIvisionEorro 가 발생합니다.
'''
>>> a / b
# Tracebak (most recent call last) :
    file "<stdin>", line 1, in <module>
  Zero DivisionError: division by zero
'''
# 그런데 이 나눗셈 계산을 아래처럼 and의 오른쪽 항에 넣으면 오류가 생기지 않습니다
'''
>>> (a * b) > 0 and (a / b) > 0
False
'''
# 파이썬이 '왼쪽 항을 평가해 보니, 오른쪽 항은 평가할 필요가 없겠구나' 하고 넘어가 버린 것이죠.
# 위 문자의 순서를 바꿔서 나눗셈을 먼저 시켜보면 ZeroDivisionError 가 발생하는 것을 볼수 있습니다.
'''
>>> (a / b) > 0 and (a * b) > 0
Tracback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDIvisionErorr: division by zero
'''