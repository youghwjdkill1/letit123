""" 문제 """
# 고무 공을 100미터 높이에서 떨어뜨리는데, 이공은 땅에 닿을 떄마다 원래 높이의 3/5만큼 튀어오릅니다.
# 공이 열 번 튈 동안, 그때마다 공의 높이를 계산합니다.

# 1   60.0
# 2   36.0
# 3   21.599999999999999999998
# 4   12.959999999999999999999
# 5.  7.7775999999999999999999 
# 6.  4.6655999999999999999995
# 7.  2.7993599999999999999996
# 8.  1.6796159999999999999998
# 9.  1.0077695999999999999998
# 10. 0.6046617599999999999998

# round() 함수를 사용해서, 다음과 같이 소수점 아래 네 자리까지 출력해 보세요.

# 1   60.0
# 2   36.0
# 3   21.6
# 4   12.96
# 5.  7.7776 
# 6.  4.6656
# 7.  2.7994
# 8.  1.6796
# 9.  1.0078
# 10. 0.6047

""" Tip """
# round()는 다음과 같이 반올림 해주는 함수입니다

# >>> round(1.23456, 2) # 1.23456을 소수점 둘째 자리로(셋째 자리에서) 반올림 # 1.23
# >>> round(1.23456, 3) # 1.23456을 솟점 셋째 자리로(넷째 자리에서) 반올림 # 1.235

# 참꼬로, 'round(2.675,20)를 수행하면 결과가 2.68 이 아닌 2.67로 나오는데, 이것은 버그가 아니라 부동소수점 연산의 한계입니다

# >>> round(2.675, 2)   # 2.67

# 지금은 150번줄에 정답있어요

height = 100
bounce = 3/5

count = 1

while count <= 10:
    height = height * bounce
    print(count , round(height, 4))
    count += 1











































































































height = 100
bounce = 3 / 5

i = 1

while i <= 10:
    height = height * bounce
    print(i, round(height, 4))
    i = i + 1