# 파일을 열 때 with문을 많이 사용한다.
# with문은 파일을 열면 파일을 자동으로 닫아주므로 f.close() 사용하지 않아도 된다.
# with문 형식 :
# with open('파일명', '열기모드', 옵션) as 객체변수명:
#     파일 처리 부분

# 1.  f = 잘라내고 그 자리에 with를 쓴다.
# 2. open() 함수의 끝에 as 를 넣는다
# 3. 잘라낸 f=을 끝에 붙여넣고 = 을 : 으로 변경한다.
# 4. 파일처리 코드를 with문 안으로 넣는다.
# 5. f.close()는 삭제한다.

filename = 'exFile1.txt'
with open(filename, 'rt') as f :
    print(f.read())