def count_receiver(start):
    try:
        while True:
            input_value = yield start
            if input_value is not None:
                start = input_value
            start += 1
    except GeneratorExit:
        print("Generator was closed and cleaned up.")

# 제너레이터 생성
counter = count_receiver(5)

# 첫 번째 yield 까지 실행하고 시작값 받기
print(next(counter))  # 5 출력

# 10을 제너레이터로 보내고, 다음 yield까지 실행
print(counter.send(10))  # 10 출력

# 다음 값을 요청
print(next(counter))  # 11 출력

# 제너레이터 닫기
counter.close()
