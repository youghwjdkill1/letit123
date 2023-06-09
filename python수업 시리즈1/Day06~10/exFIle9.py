# 원본파일 clac.exe
# 파일 탐색기 -> 주소창에 cmd
# copy %systemroot%\system32\calc.exe .

filename1 = 'calc.txt'
filename2 = 'calc2.txt'

f1 = open(filename1, 'r')
f2 = open(filename2, 'w')

f2.write(f1.read())

f1.close
f2.close

