# filename = 'exFile1.txt'
# f = open(filename, 'rt')

# # 파일 포인터: 파일의 위치를 가지고 있는 포인터
# # 파일을 열고 읽거나 쓰면 파일 포인터는 자동으로 이동된다. (파이썬에서 자동으로 설정된다.)
# print(f.read(1))  # h
# print(f.read(1))  # e
# print(f.read(1))  # l
# print(f.read(1))  # l
# print(f.read(1))  # o
# print(f.read(1))  # x

# f.close()

# print()

# filename = 'exFile1.txt'
# f = open(filename, 'rt')
# print(f.read(2))  # he
# print(f.read(2))  # ll
# print(f.read(1))  # o
# f.close()

# print()


# # while문 이용해서 출력한다.
# filename = 'exFile1.txt'
# f = open(filename, 'rt')
# data = f.read(1)  # h
# while data:
#     print(data, end='')
#     data = f.read(1)

# f.close
 
# print()


# # 무한루프를 이용해서 출력한다.
# filename = 'exFile1.txt'
# f = open(filename, 'rt')
# while 1:     # while true:
#     data = f.read(1)
#     if data:
#         print(data)
#         print(data, end='')
#     else:
#         break

# f.close

# print()

# filename = 'exFile1.txt'
# f = open(filename, 'rt')
# while 1:
#     data = read(1)
#     if not data:
#         break
#     print(data, end='')

filename = 'exFile1.txt'
f = open(filename, 'rt')
count = 0
data = f.read(1)
while data:
    print(count, " ", end='')
    print(data)
    data = f.read(1)
    count += 1

f.close()