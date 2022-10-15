#시험 점수를 입력받았을 때 1등의 점수를 출력하는 프로그램을 작성하시오.
numList=[15,22,8,79,10,8,56,89]
numList.sort()#오름차순 정렬
print(numList)
print(numList[0])#꼴찌의 점수

numList.sort(reverse=True)#내림차순 정렬
print(numList)
print(numList[0])#1등의 점수
print('1등의 점수 :',numList[0])

print(len(numList))
#5~10사이의 숫자를 입력받을 때 1등과 꼴찌의 점수차를 출력하시오.
num1=[1,2,3,4,5,7,3,4,8]
print(len(num1))#9


print(sorted(numList, reverse=True))