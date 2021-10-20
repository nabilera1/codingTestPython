#n1=int(input())
#n2=int(input())
#print('합 : ',n1+n2)

# n1,n2=map(int, input().split())
# print('합 :',n1+n2)

#학생 수 만큼 키를 입력받아 가장 큰 키를 출력하도록 합니다.
# stuNum=int(input("학생 수 입력 :"))
# print('학생수 :',stuNum)
# height=[]
# for i in range(stuNum):
#     n=int(input())
#     height.append(n)
#
# print('입력 받은 키 : ')
# for i in height:
#     print(i, end=' ')
#
# print('키가 가장 큰 녀석 찾기 ')
# height=sorted(height)#정렬
# for i in height:
#     print(i, end=' ')
#
# print('가장 큰 키 : ',height[-1])

#알파벳을 정렬하라.
# arr=['b','c','a','f','t','e']
# print(arr)
# arr=sorted(arr,reverse=True)
# print(arr)
# print(arr[0])
# print(arr[-1])
# 아래 방법 사용
# arr.sort()
# print(arr)

stack=[]
#스택에 넣을 때 5 3 2 9
stack.append(5)
stack.append(3)
stack.append(2)
stack.append(9)
#뺄 때는 9 2 3 5
print('스택에서 팝(pop)')
print(stack[::-1])
# print(stack.pop(), end=' ')
# print(stack.pop(), end=' ')
# print(stack.pop(), end=' ')
# print(stack.pop(), end=' ')




