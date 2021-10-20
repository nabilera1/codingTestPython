# 알파벳을 정렬하라
arr=['b','c','a','f','t','e']
print(arr)
#정렬
arr.sort(reverse=True)
# arr.sort()
# print(arr)
print(arr[0])
# 자료 중 아스키 코드값이
# 가장 작은 알파벳 출력
print(len(arr)) #배열의 길이 출력

# [문제] :
# 아래 알파벳 리스트 중 가장 빨리 나오는 것과
# 마지막에 나오는 알파벳을 출력하시오.
# arr=['t','b','c','k','u','n']

arr=['t','b','c','k','u','n']
arr.sort()
print(arr)
n=len(arr)-1
print(arr[0],arr[n])
# print(arr[0],arr[len(arr)-1])