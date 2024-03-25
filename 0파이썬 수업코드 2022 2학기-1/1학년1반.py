#자신의 컴퓨터 C:\1  폴더가 있어야 함.

# f = open("C:/1/newfile.txt", 'w')
# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" % i
#     f.write(data)
# f.close()

# C:\Users\user\PycharmProjects\codingTestPython\코딩테스트학습\file
# f = open("../2024 파이썬 기초/newfile.txt", "w")
# for i in range(1,11):
#     f.write(f'{i}번째 줄입니다.\n')
# f.close()
#
# f = open("../2024 파이썬 기초/newfile.txt", "r")
# print(f.read())
# f.close()


newtxt = ""
with open("test.txt","r") as file:
    oldtxt = file.readlines()
    print(oldtxt)
    for str in oldtxt:
        str = str.replace("java","python")
        newtxt += str
print(newtxt)
with open("test.txt","w") as file:
    file.write(newtxt)