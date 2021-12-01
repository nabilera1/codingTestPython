# sort() 매개변수(parameter)에 대해
# sorted()

arr=[5, 4, 8, 3] #list
arr.sort() # arr리스트 내용 변경
print(arr)

arr=[5, 4, 8, 3] #list
print(sorted(arr)) # arr 내용 변경 없음
print(arr)

arr=['김철수','박효신','BTS','이문세']
print(sorted(arr))
print(sorted(arr, reverse=True))

# 정렬을 위해 함수를 정렬 기준으로 사용해보자. key
arr=['banana','apple','pineapple','peach', 'pear']
print(*sorted(arr, key=len))
# pear apple peach banana pineapple
print(*sorted(arr, key=lambda x:x[2]))
# peach pear banana pineapple apple

# 문제 아래와 같이 정렬되도록 하시오.
# pear peach banana pineapple apple
print(*sorted(arr, key=lambda x:(x[2], len(x))))

arr=[['운동장',4],['교실',2],['도서관',3],['영어실',1]]
print(*sorted(arr,key=lambda x:x[1]))
# ['영어실', 1] ['교실', 2] ['도서관', 3] ['운동장', 4]
print(*sorted(arr,key=lambda x:x[1])[1])
# 교실 2



# [문제]
# 자재 정리하기
arr=['b1234','a12','p33','p5', 'p76']
print(sorted(arr, key=lambda x:int(x[1:])))


# 물건들을 제조 번호 순으로 정렬하는 프로그램을 만들고 싶다.
# 맨 앞 문자는 제품구분이고 그 다음 숫자 부분은 제조 번호이다.
# 이 제조 번호가 빠른 순으로 정렬하시오.
# 제품구분은 a부터 z까지이고
# 제제 번호는 1에서 10000사이의 숫자이다.
goods = ['b1234', 'a12', 'p33', 'p5', 'p76']
# a12 b1234 p5 p33 p76
print(*sorted(goods, key=lambda x: (x[0], int(x[1:]))))