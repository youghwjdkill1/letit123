"""
파일명 : exLogical3.py
프로그램 설명 : 논리 연산자 예제 3
"""

# 나이: age
# 9세이상 ~ 12세 이하
age = 13  # 8: F , 9 ~ 12: T 13~ F
print(age >= 9 and age <= 12)
print()

# 나이: age
# 8세미만 , 11세 초과
# age = 7 #True
# age = 8 #False
# age = 11 #False

print(age < 8 or age > 11)
