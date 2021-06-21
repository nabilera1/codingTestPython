import re

p = re.compile('[A-Za-z]+')
# 대소문자
m = p.match('Python1')
print(m)
if (m is None): #소스코드 다시 작성
    print("찾을 수 없음")
else:
    print(m[0])  # Python
    print(m[0][5])  # n


#https://www.pythontutorial.net/advanced-python/python-none/