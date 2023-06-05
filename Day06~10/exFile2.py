# 저장된 파일: exFile.txt
filename = 'exFile1'
# 1. 파일 열기 (읽기 모드)
# 파일이 존재하지 않으면 에러가 발생된다. (주의!)
# 파일이 존재하면 에러가 발생되지 않는다
# r, rt: 읽기 권한
# filename 변수에 저장된 파일을 읽기 모드로 연다.
f = open(filename, 'rt')

# 2. 파일 처리 (읽기)
# 형식:
# 변수명.read(): 파일 전체 일기
# 변수명.read(size): 파일의 size 만큼 읽기
# 리턴값: 읽은 문자열으 반환한다.
#
# read() 메소드(함수)는 리턴값이 있으므로 두가지 방식을 사용하다
# 리턴값을 바로 출력하는 경우: print(f.read())
# 리턴값을 변수에 저장해서 활용하는 경우
# data = f.read()    # "hello"
# print(data)
print(f.read())

# 3. 파일 답기
# 형식:
# 변수명.close()
f.close()

# 파일 포인터: 파일의 위치를 가지고 있는 포인터
