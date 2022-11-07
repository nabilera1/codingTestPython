#자신의 컴퓨터 C:\1  폴더가 있어야 함.

# f = open("C:/1/newfile.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# C:\Users\user\PycharmProjects\codingTestPython\코딩테스트학습\file
f = open("./file/newfile1.txt", "w")
for i in range(1,11):
    f.write(f'{i}번째 줄입니다.\n')
f.close()

#open and read the file after the writing or appending:
f = open("./file/newfile1.txt", "r")
print(f.read())
