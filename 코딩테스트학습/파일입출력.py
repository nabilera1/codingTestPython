# f = open("C:/doit/새파일.txt", 'w')
# FileNotFoundError: [Errno 2] No such file or directory: 'C:/doit/새파일.txt'
# f.close()

"""
현재 이 디렉토리 경로
- 파이참 : ctrl + alt + f12
C:\\Users\\user\\PycharmProjects\\codingTestPython\\코딩테스트학습
C:/Users/user/PycharmProjects/codingTestPython/코딩테스트학습
단축키
Ctrl + E : 최근 파일
Alt + Home
"""

# f = open("newfile.txt", "w")
# # 파이참 코드의 현재 경로에 파일이 생김.
# # 코랩이라면 구글 드라이브에 생김.
# f.write("오늘은 좋은 날")
# f.close()
#
# #open and read the file after the writing or appending:
# f = open("newfile.txt", "r")
# print(f.read())

# 2번째 코드
# file 폴더는 있어야 함.
# 예: c:/file
f = open("./file/newfile1.txt", "w")
for i in range(1,11):
    f.write(f'{i}번째 줄입니다.\n')
f.close()

#open and read the file after the writing or appending:
f = open("./file/newfile1.txt", "r")
print(f.read())