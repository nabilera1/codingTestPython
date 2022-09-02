#ord : 유니코드 정수
#chr : 유니코드 문자

print(ord('a'))#97
print(ord('A'))#65

print(chr(99))#c

#소문자 출력
for i in range(97, 123):
    print(chr(i),end=' ')
print()
for i in range(0, 26):
    print(chr(ord('a')+i), end=' ')