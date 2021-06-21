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

