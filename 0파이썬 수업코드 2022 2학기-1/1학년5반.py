# a = [1, 2, 3, 1, 2, 3]
# a.pop(7)
# print(a)

# money=2000
# card=True
# if money>=3000 or card:
#     print('택시')
# else:
#     print('조깅')

# print('a' in 'python')
# print('t' in 'python')

# pocket=['paper', 'cellphone', 'money']
# if 'money' in pocket:
#     pass
# else:
#     print('조깅')

# a = "Life is too short, you need python"
# if "wife" in a: print("wife")
# elif "python" in a and "you" not in a:
#     print("python")
# elif "shirt" not in a:
#     print("shirt")
# elif "need" in a:
#     print("need")
# else:
#     print("none")
#
#

# [1, 2, 3, 4, 5, 6, 7, 8, 9]를 만드시오.
# a = range(1, 10)
# print(a)
# print(type(a))
# b = list(a)
# print(b)
# print(type(b))
# # print(type(1))

# print(*list(range(1, 101)))
# print(list(range(1, 101)))
# print(*range(1, 101))
# print(range(1, 101))
# print(sum(range(1, 101)))

# li = [1, 2, 3, 4]
# print(li)
# # 제곱
# print([i * i for i in li])
# # 1~20사이의 짝수만 뽑아서 3을 곱한 결과 출력하시오.
# print([i * 3 for i in range(1, 21) if i % 2 == 0])
#
# print(type((1)))
# print(type((1,)))
#
# # a='test'
# print(f'{"test":-^20}')

# 딕셔너리

# 빈 리스트, 빈 튜플, 빈 딕셔너리
# 빈 셋
# s = set()
# d  = {}
# d1 = dict()
# s = set([1, 2, 3])
# print(s)
# 딕셔너리와 셋의 차이점은 무엇일까?
# 인덱스로 접근이 가능할까?
# s = list(s)
# print(s[0]) #셋이라면 에러 발생
# name에 자기 이름을 영어로 셋 자료형에 넣어보시오.
# 그리고 출력하시오.
# name = input()
# name = set(name)

# 영어 알파벳을 정렬하여 출력해 보세요.


# 교집합, intersection, &
# print(f'교집합:{s1 & s2}')
# print(f'교집합:{s1.intersection(s2)}')

# 합집합, union, |

# 차집합, difference, - (순서)

# 셋 자료형의 add, update
l1 = [1, 2, 3, 4, 5, 6, 3, 4]
s1 = set(l1)
print(s1)
s1.add(7)
print(s1)
s1.update([6, 7, 8, 9])
print(s1)
s1.remove(6)
print(s1)
# s1.remove(6)  #KeyError
s1.discard(6)
print(s1)
#
# print(s1)
# print(len(s1))
# print(s1.pop()) #FIFO
# print(s1.pop())
# print(s1.pop())
# print(s1)
# s1.clear() #None
# # del s1 이라고 하면 s1이 메모리에서 제거
# print(s1)
#
#
