# https://pynative.com/python-list-quiz/
'''
Python List Exercise.

This quiz contains 16 Questions. Solve 11 correct to pass the test.
You will have to read all the given answers and click over the correct answer.
Read the guide on Python Lists to solve this quiz.

'''
print(2 ** 365)

# 리스트의 내용을 출력할 때 각 요소별 /를 넣어서 출력하시오.
data = 'korea'  # ['korea'] 와 차이점
print(','.join(data))

data = ["I", "like", "Coding"]
print("-".join(data))

data = ["Hello", "Python", "Coding"]
# [출력 예시]
# Hello/Python/Coding
print("/".join(data))

num = [10, 20, 30, 40]
num.pop()
print(num)

# 샘플에서 숫자를
num = [10, 20, 30, 40, 50, 60, 70, 80]
num.pop()
print(num)

print('-' * 30)
li = [5, 2, 7, 3]
li.sort()
print(li[0])

num.pop(2)
print(num)

# What is the output of the following code

list1 = ['tiger', 'zibra', 'Python']
print(max(list1))

# What is the output of the following list comprehension

d = [x + 5 for x in [1, 2, 3]]
print(d)
# [6, 7, 8]
d = [x + y for x in [1, 2, 3] for y in [5, 6]]
# print(d)
# [6, 7, 7, 8, 8, 9]
print('sum=', sum(d))


d = [x + y for x in ['My ', 'Your '] for y in ['Love', 'Destiny']]
print(d[1])

# What is the output of the following list function?

sampleList = [10, 20, 30, 40, 50]
sampleList.append(60)
print(sampleList)

sampleList.append(60)
print(sampleList)

# Select all the correct options to join two lists in Python
list1 = ['a', 'b', 'c', 'd']
list2 = ['e', 'f', 'g']

# newList=listOne + listTwo
newList = list1.extend(list2)  # 차이점
print(newList)
print(list1)

# What is the output of the following list operation
nList = [10, 20, 30, 40, 50, 60, 70, 80]
print(nList[2:5])
print(nList[:4])
print(nList[3:])

# What is the output of the following list operation
sampleList = [10, 20, 30, 40, 50]
print(sampleList[-2])
print(sampleList[-4:-1])

# What is the output of the following list assignment
nList = [4, 8, 12, 16]
nList[1:4] = [20, 24, 28]
print(nList)

# Select all the correct options to copy a list

arr1 = ['a', 'b', 'c', 'd']
arr2 = arr1.copy()
print(arr2)

# What is the output of the following code

nList = ["PYnative", [4, 8, 12, 16]]
print(nList[0][1])
print(nList[1][3])

# What is the output of the following code?
sampleList = [10, 20, 30, 40]
del sampleList[0:4]
print(sampleList)

# What is the output of the following?
nList = [1, 2, 3, 4, 5, 6, 7]
pow2 = [2 * x for x in nList]
print(pow2)

# What is the output of the following
l = [None] * 10
print(l)
print(len(l))

# What is the output of the following
nList = [5, 10, 15, 25]
print('aaaa', nList[::])
print('aaaa', nList[::2])
print('aaaa', nList[::-2])

# 출력결과를 작성하시오.
a = list(range(5))
b = list(range(5))
# 리스트를 그냥 더하면
print(a + b)

li = list()
li = [a[i] + b[i] for i in range(len(a))]
print(li)

# The zip() function takes iterables (can be zero or more), aggregates them in a tuple, and return it.
a = [1, 2, 3]
b = [5, 6, 7]
print(list(zip(a, b)))
# zip : 인덱스가 같은 요소끼리 튜플로 묶기
z = zip(a, b)
li = list()
for n1, n2 in z:
    li.append(n1 + n2)
print(li)

'''
위 for문을 리스트 컴프리헨션으로 작성한다면 아래와 같이 작성할 수 있다.
리스트 컴프리헨션도 기억해두자.

print([n1+n2 for n1,n2 in z])
'''
