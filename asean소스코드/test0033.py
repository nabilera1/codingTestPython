fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.count('banana'))
print(fruits.count('tomato'))
print(fruits.index('apple'))
print(fruits.index('apple',2))
fruits.reverse()
print(fruits)
print(fruits.sort())
print(fruits)
print(fruits.pop())
print(fruits)

# [문제]
# fruits 리스트에 ‘tangerine’ 과일을 추가하고, 다시 정렬하는 코드를 작성하시오.
fruits.append('tangerine')
fruits.sort()
