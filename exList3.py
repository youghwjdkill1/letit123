"""
파일명:exList3.py
프로그램 설명: 리스트 메소드를 사용하는 방법 
"""

#리스트 메소드 형식:
# 변수명 . 메소드()
listData = []
listData.append(1)
listData.append(2)
listData.append(3)
listData.append(4)
listData.append(5)
print(listData) # [1, 2, 3, 4, 5]
listData.pop()
print(listData) # [1, 2, 3, 4]
listData.remove(1) #인덱스 위치가 아니라 Data 1을 삭제한다
print(listData) # [2, 3. 4]
listData.clear()
print(listData) #[]
