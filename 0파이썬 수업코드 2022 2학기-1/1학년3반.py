# lst = ['Apple', 'Banana', 'Orange']
# print(', '.join(f'{x}s' for x in lst))

# a = input()
# # a.upper()
# a = a.lower()
# print(a)

# a = '개울가에 소년이 나타났다. 소녀는 개울가를 건너고자 한다.'
# a = a.replace(' ', '')
# print(a)
# print(len(a))

# a = 1
# print(type(a))
# arr = [1, 2, ['a', 'b', ['Life', 'is']]]
# print(arr[-1])
# print(arr[2])
# 1에서 1000까지의 3의 배수의 총합은?
# print(sum([x for x in range(1, 1001) if x % 3 == 0]))
#
#
# t = 1
# print(type(t))
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = [1]
# print(type(t))

# d = {}
# print(type(d))
# dic = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
# print(dic)
# # 1 는 대구시
# dic[1] = '대구시'
# print(dic)
# print(dic[1])


# d = {}
# k = input()
# d[k] = input()
# print(d)
# https://docs.python.org/ko/3/library/pprint.html
#
# none None 비교
#
l1 = [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7, 6, 7]
s1 = set(l1)
s2 = set(l2)
print(s1)
print(s2)
# 교집합, intersection, &
print(f'교집합 : {s1.intersection(s2)}')
print(f'교집합 : {s1 & s2}')

# 합집합, Union, |

# 차집합, difference, - (순서에 따라 결과가 다름)

# SET에 add, update
print(s1)
s1.add(6)
print(s1)
s1.add(6)
print(s1)

s1.update([5, 6, 7, 8])  # s1.update(8)  TypeError
print(s1)
# s1 = s1 + 4
# s1 = s1 + {4}
s1 = s1 | {4}


#
# print([x for x in range(1,10)])
# print(x for x in range(1,10))
# print(set(x for x in range(1,10)))
# print(set([x for x in range(1,10)]))
# print(set(range(1,10)))

def add_mul(*args):
    if args[0] == "add":
       result = 0
       for i in args[1:]:
           result = result + i
    elif args[0] == "mul":
        result = 1
        for i in args[1:]:
            result = result * i
    return result

print(add_mul('add',1,2,3))

