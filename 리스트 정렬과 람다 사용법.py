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
