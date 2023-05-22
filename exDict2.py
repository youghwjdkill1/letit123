"""
파일명 : exDict2.py
프로그램 설명: 딕셔너리 자료형
"""

# 키가 중복된 경우
# 처음에 만들어진 키는 인식하지 않고 나중에 만들어진 키만 인식된다.
dictData = {'a':1, 'a':2, 'b':3, 'b':4, 'e':5}
print(dictData)  # {'a': 2, 'b': 4, 'e': 5}
for key in dictData:
    print(key)  # a b e
for value in dictData.values():
    print(value)  # 2 4 5 (키 중복에 의해서 1, 3은 출력되지 않는다.)


dictData = {'a':1, 'b':1, 'c':1, 'd':2, 'e':2}

for value in dictData.values():
    print(value)  # 1 1 1 2 2 

# kor: 국어점수, eng: 영어점수, math: 수학점수
dictData = { 'kor':100, 'eng':100, 'math':100 }

for value in dictData.values():
    print(value)  # 100 100 100

# 딕셔너리에 키와값을 추가하는 형식:
# 변수명['키'] = 값 or # 변수명[키변수명] = 값
dictData = {}  # 빈 딕셔너리
dictData['kor'] = 1
dictData['eng'] = 2
dictData['math'] = 3

print(dictData)

# 딕셔너리에 키와값을 추가하는 형식:
# 변수명['키'] = 값 or # 변수명[키변수명] = 값
dictData = {}  # 빈 딕셔너리
dictData['kor'] = 1
dictData['eng'] = 2
dictData['math'] = 3

# 딕셔너리에 키를 삭제하는 형식:
# 변수명.pop('키') or 변수명.pop(키변수명) 
# del(변수명['키']) or del(변수명[키변수명])
dictData.pop('math')
print(dictData)
del(dictData['kor'])
print(dictData)
