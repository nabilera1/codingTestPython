from copy import copy

# 원본 리스트
original_list = [1, 2, 3, 4, 5]

# 리스트 복사
copied_list = copy(original_list) #copy 모듈 사용
#copied_list = original_list.copy() #리스트 타입의 내장 메서드 사용

# 복사된 리스트 출력
print("원본 리스트:", original_list)
print("복사된 리스트:", copied_list)

copied_list[1] = 7

print(copied_list)
print(original_list)