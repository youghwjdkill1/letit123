def myMax(a, b):
    if a > b:
        return a
    else:
        return b
    
print(myMax(1,2))    # 2
print(myMax(100,2))  # 100
print(myMax(100,2,200))  # 에러 (인수를 2개 밖에 받을 수 없다.)

def myMax(*args):
    a = 0

    for b in args:  # 튜플은 반복
        if a > b:
            a = a
        else:
            a = b
    return a
    
print(myMax(1,2))    # 2
print(myMax(100,2))  # 100
print(myMax(100,2,200))  # 에러 (인수를 2개 밖에 받을 수 없다.)