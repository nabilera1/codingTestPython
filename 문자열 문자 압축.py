

# str='AAAAAAABBCCCDEEEEFFFFFG'
# 답 A7B2C3D1E4F5G1
# aaaaaabbb
# 답 a6b3
str=input()
str1=list(set(str))
str1.sort()
# print(str1)
for i in range(len(str1)):
	print(str1[i], end='')
	print(str.count(str1[i]), end='')