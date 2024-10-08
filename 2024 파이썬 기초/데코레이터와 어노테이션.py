
#decorator
def deco1(func):
    def wrapper1():
        print("함수가 호출되기 전에 실행됩니다.")
        func()
        print("함수가 호출된 후에 실행됩니다.")
    return wrapper1

@deco1
def say_hello():
    print("안녕하세요!")

say_hello()


# annotation

def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(3, 5)
print(result)