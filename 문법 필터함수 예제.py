# 필터함수에 일반함수와 람다함수 적용
arr = ['a', 1, 2, 'b', 13, 17, 'c', 2.5, 7.9]

def f1(arr):
    if isinstance(arr, int):
        return True
    return False


def f2(arr):
    if isinstance(arr, float):
        return True
    else:
        return False


def f3(arr):
    return isinstance(arr, str)
ans=list(filter(f3,arr))
ans1=list(filter(f2,arr))
print(f'리스트 속 문자 : {ans}')
print(f'리스트 속 실수 : {ans1}')
ans3=list(filter(f1,arr))
print(f'리스트 속 정수 : {ans3}')
ans3=list(filter(lambda n: n<5, ans3))
print(f'리스트 속 5 미만 정수 : {ans3}')