# num = input()
# # a = "I eat {0} apples".format(num)
# # a = "I eat {} apples".format(num)
# print("I eat {0} apples".format(num))
#
# # % 를 사용하여 동일하게 보이도록 해 보시오.
# print("I eat %s apples" % (num))
# print(f"I eat {num} apples")
# print(f'I eat {num} apples')
# n = 4.567173
# print("{0:0.4f}".format(n))
# print("{:0.4f}".format(n))
# print(f"{n:0.4f}")
# print(f"{n}")
# # print("{0:=^50}".format("Multiplication Table"))
# n1, n2 = map(int, input().split())
# print('=' * 10)
# print(f'''{n1:>10}
# X{n2:>9}
# {'-'*10}
# {n1 * n2:>10}''')
# print('=' * 10)
# print(f'''{n1:>10}
# +{n2:>9}
# {'-'*10}
# {n1 + n2:>10}''')
# print('=' * 10)

# a = '개울가에 소년이 나타났다. 소녀는 개울가를 건너고자 한다.'
# print(a.count(' '))
# print(a.replace(' ',''))
# print(a.replace('개울가', 'PC방'))
# a = a.replace('개울가', 'PC방')
# print(a)
# print(a.find('소년'))
# print('청소년 검색 : ', a.find('청소년'))
#
# print(a.index('소년'))
# print('청소년 검색 : ', a.index('청소년'))


# 소년은 6번째에 나옵니다.
# print(f"소년은 {a.find('소년')+1}번째에 나옵니다.")
a = [1, 2, 3]
a.append(4)
a.append(5)
print(a)
