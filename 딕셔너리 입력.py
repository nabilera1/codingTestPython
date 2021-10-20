#딕셔너리 입력 후 생성
#1 kim 2 hong 3 lee
hash={}
for _ in range(3):
    key, value=input().split()
    hash[int(key)]=value
print(hash)

# 1 a
# 2 b
# 3 c
# {1: 'a', 2: 'b', 3: 'c'}

# 딕셔너리?
# [키, 값] 쌍을 담아두는 자료구조이다.
# 키는 원소를 찾기 위한 식별자이다.
# 딕셔너리와 해시는
# 유일한 값(반복되지 않는 값)만 저장한다.