""" 연습문제 : 나이에 따른 세대 구분(1) """
# 'input()' 으로 사용자의 나이를 입력받은 후, 다음 표의 어느 세대에 속하는지 출력 하세요.
# 입출력 문구는 자유롭게 지으면 됩니다.

# 출생연도       세대
# ~ 1924        가장 위대한 세대(The Freatest Generation)
# 1925 ~ 1945   침묵 세대 (The Slient Generation)
# 1946 ~ 1964   베이비붐 세대 (baby boomer)
# 1965 ~ 1980   X 세대 (Generatio X)
# 1981 ~ 1996   밀레니얼(milennial)
# 1997 ~ 2002   Z 세대(Generation Z)
# 2003 ~ 2023   MZ 세대(Generation MZ)

""" 예 1 """
# $ python3 generations1.py
# What year were you born? 1945
# You're the Silent Generation

""" 예 2 """
# $ python3 generations1.py
# What year were you born? 1946
# You're a baby boomer

""" 예 3 """
# $ python3 generations1.py
# What year were you born? 1964
# You're a baby boomer

""" 예 4 """
# $ python3 generations1.py
# What year were you born? 1965
# You're a Gen X.

""" 정답 맞쳐보는 곳 """



















































































































""" 정답 """

y = int(input('What year were you born? '))

gen = None

if y <= 1924:
    gen = 'the Greatest Generation'
elif y <= 1945:
    gen = 'the Silent Generation'
elif y <= 1964:
    gen = 'a baby boomer'
elif y <= 1980:
    gen = 'a Gen X'
elif y <= 1996:
    gen = 'a millennial'
else:
    gen = 'a Gen Z'

print(f"You're {gen}.")