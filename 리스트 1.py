li=[]
li.append('BTS')
li.append('MJ')
li.append('Beatles')
print(li)

for i in range(0,3,1):
    li.append(input('이름을 쓰세요 : '))

print('-'*20)
print(li)
print(len(li),'개')
print('5번째',li[4])
print('6번째 %s' %li[5])
