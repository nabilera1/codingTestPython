from sympy import is_carmichael

def find_carmichael_numbers(limit):
    """특정 범위 내에서 모든 카마이클 수를 찾는 함수"""
    carmichael_numbers = []
    for number in range(2, limit):
        if is_carmichael(number):
            carmichael_numbers.append(number)
    return carmichael_numbers

# 범위 설정 (예: 10000까지)
limit = 10000
carmichael_numbers = find_carmichael_numbers(limit)

# 결과 출력
print(f"Carmichael numbers up to {limit}: {carmichael_numbers}")