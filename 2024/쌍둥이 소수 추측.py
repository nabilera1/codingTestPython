def is_prime(n):
    """주어진 숫자가 소수인지 확인하는 함수"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    """지정된 범위 내에서 모든 쌍둥이 소수를 찾는 함수"""
    twin_primes = []
    for n in range(2, limit - 2):
        if is_prime(n) and is_prime(n + 2):
            twin_primes.append((n, n + 2))
    return twin_primes

# 최대 범위를 지정하고 쌍둥이 소수를 찾는다
limit = 1000  # 예시로 1000까지의 범위를 사용
twin_primes = find_twin_primes(limit)

# 결과 출력
for twin in twin_primes:
    print(f"{twin[0]}, {twin[1]}")
