filename = "exfile.txt"

# 1. 파일 열기 (추가모드)
# 파일이 존재하면 기존에 저장된 파일의 끝에 추가된다.
# 파일 포인터(파일의 위치)는 파일의 끝으로 이동한다.
# 파일이 존재하지 않으면 새로운 파일이 생선된다.
# 형식 : 
# 변수명 = open('파일명', 'a', 옵션)
# w: 쓰기모드
# r: 읽기 모드
# a: 추가 모드
filename = "exFile.txt"
openFile = open(filename, 'a')

# 2. 파일 처리 (추가)
data = "안녕하세요! 즐거운 파이썬 시간입니다."
print(data, len(data))  # 안녕하세요! 즐거운 파이썬 시간입니다. 21
openFile.write(data)

# 3. 파일 닫기
openFile.close()
