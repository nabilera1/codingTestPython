#문자열
str1 = "Life is too short"
str2= ", You need python."
sentence = str1 + str2
print(sentence)

# [문제]
# 글자의 길이를 출력해 보세요.
print(len(sentence))
q='python' in sentence
print(q)

n=sentence.find('is')
print(n)
n=sentence.find('You')
print(n)

print(sentence[3]) #Life  <-- e

print(sentence.replace('You','I'))

t1=sentence.upper()
print(t1)

t2=sentence.lower()
print(t2)

print(t1,t2)

# [문제]
# sentence에서 ‘python’을 ‘you’로 바꾸어 출력해 보세요.
print(sentence.replace('python','you'))