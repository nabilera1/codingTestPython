# def f1(s):
#     r = ''
#     for txt in s:
#         r += txt + ' '
#     return r.strip()  # 문자열 리턴
#
#
# mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']
#
# sentence = f1(mydata) #문자열
# print(sentence)
#
# newSen = sentence.replace('Coding', 'Programming')
# print(newSen)

# 리스트의 내용을 바로 변경해보자.
mydata = ['Hello,', 'I', 'like', 'Python', 'Coding']

idx = 0
for txt in mydata:
    if 'Coding' in txt:
        break
    idx += 1

mydata[idx] = 'Programming'

print(mydata)
print(*mydata)



