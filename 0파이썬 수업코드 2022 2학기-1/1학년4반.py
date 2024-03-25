# 파일 입출력

# 절대경로 / 상대경로
#fn = 'c:/1/mydiary.txt' # 절대경로
fn = '../2024 파이썬 기초/mydiary.txt' # 상대경로
f = open(fn,'w') # 파일 생성
f.write('오늘의 일기\n')
f.close()
# 내일은 주말이다. 를 추가하는 코드를 작성하시오.
f = open(fn, 'a')  # 파일에 내용 추가
f.write('내일은 주말이다.\n')
f.close()
f = open(fn, 'r') # 파일 읽기
print(f.read())
f.close()


