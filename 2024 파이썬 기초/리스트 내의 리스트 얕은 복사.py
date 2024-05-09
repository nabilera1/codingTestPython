from copy import copy

# 중첩 리스트
nested_list = [1, 2, [3, 4]]

# 중첩 리스트의 얕은 복사
shallow_copied_list = copy(nested_list)
# 리스트 복사
# shallow_copied_list = nested_list.copy()

# 내부 리스트 변경
shallow_copied_list[2][0] = "변경됨"

# 변경 후의 원본 및 복사 리스트 출력
print("원본 리스트:", nested_list) #리스트 내부 리스트의 참조 공유되고 있음. 함께 변경됨.
print("얕은 복사된 리스트:", shallow_copied_list)


# 원본 리스트
original_list = ['a', 'b', 'c']

# 리스트 복사
copied_list = copy(original_list)

# 원본 리스트 변경
original_list.append('d')

# 변경 후의 원본 및 복사 리스트 출력
print("원본 리스트 변경 후:")
print("원본 리스트:", original_list)
print("복사된 리스트:", copied_list)