# 5명이 출입구에 모이면 번호가 큰순으로
# 들여보내야 한다.
# 이 때 중복된 번호의 학생은 한 명만 안으로 보내도록 하자.
# [입력] : 4 5 1 2 3
# [출력] : 5 4 3 2 1


# [입력] : 3 5 1 2 3
# [출력] : 5 3 2 1

# [입력] : 14 5 7 2 3
# [출력] : 14 7 5 3 2

students = list(set(map(int, input().split())))
students.sort(reverse=True)
for i in students:
    print(i, end=' ')