# 제어문 : if문
# a=5
# if a > 3:
#     print('3보다 큼')
# else:
#     print('3보다 작음')
# 라인 정렬 : ctrl + alt + L

# 숫자를 하나 입력받아 70이상이면 최우수
# 그 외 50이상이면 우수
# 그 외 20이상이면 보통
# 그 외는 노력 필요를 출력하는 프로그램
a = int(input())
if a >= 70:
    print("최우수")
elif a >= 50:  # elif ==> else if
    print("우수")
elif a >= 20:
    print("보통")
else:
    print("노력 필요")

# 두 숫자를 입력 받아 더 큰 수를 출력하는 프로그램을 만드시오.
# [입력] 8 3
# [출력] 8
