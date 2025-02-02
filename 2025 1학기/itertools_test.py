import itertools

# 여러 iterable 객체를 연결
list1 = [1, 2, 3]
tuple1 = (4, 5, 6)
set1 = {7, 8, 9}

# itertools.chain 사용
result = itertools.chain(list1, tuple1, set1)

# 연결된 iterator 출력
print(list(result))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(result)
print(type(result))


import itertools

numbers = [1, 2, 3]
words = ["one", "two", "three"]

result = itertools.chain(numbers, words)
print(list(result))


print('-'*30)

import itertools

numbers = [10, 20]
letters = "AB"
words = ("hello", "world")
single_number = [100]

result = itertools.chain(numbers, letters, words, single_number)

print(list(result))


import itertools

nested_list = [[1, 2, 3], [4, 5], [6]]
string = "XYZ"

result = itertools.chain(*nested_list, string)

print(list(result))
