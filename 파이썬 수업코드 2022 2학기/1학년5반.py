# # num을 입력받아 보세요.
# # num = int(input())
# num = input()
# a = "I eat {0} apples".format(num)
# a = "I eat {} apples".format(num)
# print(a)
# # % 를 사용하여 동일하게 보이도록 해 보시오.
# print("I eat %s apples" % (num))
# print(f"I eat {num} apples")

# dictionary    key, value 한쌍
# d = {'apple': '사과', 'age': 30}
# print(f"나의 이름은 {d['apple']}입니다. 나이는 {d['age']}입니다.")

# a, b = map(int, input().split())
# print(f"{a:>10}")
# print(f"*{b:>9}")
# print("-" * 10)
# print(f"{a * b:>10}")


# a = '개울가에 소년이 나타났다. 소녀는 개울가를 건너고자 한다.'
# # print(a.count('개울가'))
# a = a.replace('개울가', 'pc방')
# print(a)
# print(a.replace(' ',''))


a = ['1', 3, 'ab']
a.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
