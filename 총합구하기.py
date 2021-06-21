#숫자를 입력받아 총합을 구하는 프로그램을 만드시오.
#1 2 3 4
#10
num=[0]*11
print(num)
for n in range(1,11):
    num[n]=n
print(num)
print(sum(num))
