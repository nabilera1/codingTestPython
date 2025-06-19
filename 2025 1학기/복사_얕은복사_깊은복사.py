import copy


def modify(x):
    x[0] = 42
    y = x[:]
    y[0] = 5

original = [10]     # 리스트로 감쌈
modify(original)
print(original[0])  # 42


def modify2(x):
    x[0][0] = 42
    y = x[:]
    y[0][0] = 5

original = [[10]]     # 리스트 내부에 리스트로 감쌈
modify2(original)
print(original[0][0])  # 5