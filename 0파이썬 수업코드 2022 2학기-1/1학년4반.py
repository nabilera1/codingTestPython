# f = open("c:/1/newfile.txt", 'w')
# for i in range(1, 11):
#     data = f'{i}번째 줄입니다.\n'
#     f.write(data)
#
# f.close()
f = open("c:/1/mydiary.txt", 'r', encoding='utf-8') #cp949
# print(f.read())
lines = f.readlines()
print(lines)
for line in lines:
    line = line.strip()
    print(line)

f.close()