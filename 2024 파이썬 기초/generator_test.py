# 숫자를 순차적으로 생성하는 제너레이터 함수 정의
def generate_numbers(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

# 제너레이터 사용 예제
for number in generate_numbers(1, 5):
    print(number)


g=generate_numbers(11, 15)
print(next(g)) # 11
print(next(g)) # 12


# 참조
print(generate_numbers(11, 15).__next__()) # 11
print(generate_numbers(11, 15).__next__()) # 11


print(next(generate_numbers(11, 15))) # 11
print(next(generate_numbers(11, 15))) # 11

print(range(1_000))
