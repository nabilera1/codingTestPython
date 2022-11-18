filename = 'c:/1/test1.txt'
def showFile(filename):
    f = open(filename, 'r', encoding='utf-8')
    l = f.readlines()
    print(l)
    txt=''
    for i in l:
        txt=i.strip()
        txt.replace('java','python')
        print(txt)
    f.close()

showFile(filename)


# while True: #무한 루프
#     l = f.readline()
#     if not l: #l이 파일의 끝에 도달하면
#         break
#     print(l)
# f.close()


# filename = 'c:/1/새파일.txt'
# f = open(filename, 'r')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# print(f.readline(), end='')
# f.close()










# def showFile(filename):
#     f = open(filename, 'r', encoding='utf-8')
#     l = f.readline()
#     print(l)
#     for line in l:
#         print(line)
#     f.close()
#
# filename = 'c:/1/새파일.txt'
# showFile(filename)
# # 파일에 한글을 읽을 수 있는 함수
#

#
# def showFile(filename):
#     f = open(filename, 'r', encoding='utf-8')
#     lines = f.readlines()
#     print(lines) # list
#     for l in lines:
#         print(l.strip())
#     f.close()
#
# filename="C:/1/새파일.txt"
# showFile(filename)
