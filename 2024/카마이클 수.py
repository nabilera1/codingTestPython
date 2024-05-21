# from sympy import isprime
# from sympy.ntheory.factor_ import is_carmichael
#
# def find_carmichael_numbers(limit):
#     """지정된 범위 내의 모든 카마이클 수를 찾는 함수"""
#     carmichael_numbers = []
#     for num in range(2, limit):
#         if is_carmichael(num):
#             carmichael_numbers.append(num)
#     return carmichael_numbers
#
# # 원하는 최대 범위를 설정
# limit = 10000
#
# # 카마이클 수 찾기
# carmichael_numbers = find_carmichael_numbers(limit)
#
# # 결과 출력
# print(f"Carmichael numbers up to {limit}: {carmichael_numbers}")


def is_prime(n):
    """주어진 숫자가 소수인지 확인하는 함수"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factors(n):
    """주어진 숫자의 소인수 목록을 반환하는 함수"""
    factors = set()
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return factors


def is_carmichael(n):
    """주어진 숫자가 카마이클 수인지 확인하는 함수"""
    if n < 2 or is_prime(n):
        return False

    prime_factors_list = prime_factors(n)

    # 모든 소인수 p에 대해 (n-1) % (p-1) == 0 이어야 함
    for p in prime_factors_list:
        if (n - 1) % (p - 1) != 0:
            return False
    return True


def find_carmichael_numbers(limit):
    """특정 범위 내에서 카마이클 수를 찾는 함수"""
    carmichael_numbers = []
    for num in range(2, limit):
        if is_carmichael(num):
            carmichael_numbers.append(num)
    return carmichael_numbers


# 원하는 최대 범위 설정 (예: 10000까지)
limit = 10000
carmichael_numbers = find_carmichael_numbers(limit)

# 결과 출력
print(f"Carmichael numbers up to {limit}: {carmichael_numbers}")
