# f = open("C:/1/log.txt", 'r')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()


f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()
f2 = open("test.txt", 'r')
print(f2.read())