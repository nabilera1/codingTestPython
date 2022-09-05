#[문자열 인덱싱과 슬라이싱]
a="Life is too short, You need Python"
print(a[0])
print(a[3])
print(a[-1])
print(a[-2])

#slicing
print(a[0:4]) #0~3까지
print(a[5:7]) #5~6까지

# 문제
# 문자열 슬라이싱을 통해 'short'라는 단어를 출력하세요.
print(a[12:17])

print(a[19:]) #19번째 이후 모두
print(a[:17]) #17번째 이전 모두
print(a)
print(a[:])

# [문제]
# '20250725sunny'라는 문자열에서 년월일 그리고 날씨를 추출해보세요.
a='20250725sunny'
print(a[0:4], a[4:6], a[6:8], a[8:] )