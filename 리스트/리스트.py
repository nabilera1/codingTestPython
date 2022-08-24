# 팩토리얼 구현
# 5! = 120

num = int(input("자연수 입력 : "))
fac = 1

if num < 0:
    print("1보다 큰 수를 입력해주세요.")
elif num == 0:
    print("0팩토리얼은 1입니다.")
else:
    for i in range(1, num + 1):
        fac = fac * i
    print(num, "팩토리얼은 ", fac, "입니다.")
    # print(f'{num} 팩토리얼은 {fac}입니다.')
