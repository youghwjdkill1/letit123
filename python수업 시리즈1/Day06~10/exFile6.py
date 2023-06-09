filename = "exFIle1.txt"
# 형식:
# 변수명 = open("파일명", "열기모드", encoding='utf8')
f = open(filename, 'wt', encoding='utf8')

# 2. 파일 처리 (쓰기)
print(f.write('hello 안녕하세요'))

# 3. 파일 닫기
f.close()

# utf8로 파일을 저장하면 utf8로 파일을 오픈해야 한다.
# utf8로 저장하고 cp949로 오픈하면 
