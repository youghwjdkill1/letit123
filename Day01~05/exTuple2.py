"""
파일명: exTuple.py
프로그램 설명: 튜플 자료형에 데이터를 넣는 방법
"""

a = (1,2,3,4,5)   # 정수
b = (1.2, 2.1, 3.14)  # 실수
c = ('홍길동', '고길동', '김길동')  # 문자열
d = (1, 2.3, '홍길동')  # 다른 자료형을 같이 저장할 수 있다.
e = ((1,2,3), [4,5,6])
#   e[0][0]    e[1][1]
print(a); print(b); print(c); print(d); print(e)
print(e[0][0], e[1][1])  # 1 5

# a ~ e 까지 변수를 tupleData 변수에 저장한다.
tupleData = (a,b,c,d,e)

for value in tupleData:
    print(value)

print('프로그램 종료')  