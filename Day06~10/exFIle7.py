filename = "data.txt"

# f = open(filename, 'rt', encoding='utf8')
# data = f.readline()
# while data:
#     print(data, end='')
#     data = f.readline()
# f.close()

# with문으로 한거
#with open(filename, 'rt', encoding='utf8') as f:
#    data = f.readlin())
#    with data:
#        print(data, end=' ')
#        data = f.readline()

# for문을 이용해서 좀 더 심플하게 반복해서 처리하는 경우
# with open(filename, 'rt', encoding='utf8') as f:
#     for data in f:
#         print(data, end='')

with open(filename, 'rt', encoding='utf8') as f:
    data = f.readlines()
    for line in data:
        print(line, end=' ')
