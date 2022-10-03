dict={1:'a',2:'b',3:'o',4:'d',5:'h',6:'m',7:'k',8:'i',9:'g'}
for i in range(1,10,1):
    if(i%3==0):
        print(dict[i],end='')
dict[10]='hello'
print('')
print(dict[10])
print(dict)
print("성공적으로 추가되었습니다")
