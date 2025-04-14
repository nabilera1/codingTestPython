'''

정렬된 숫자 리스트 nums와 정수 target이 주어졌을 때,
 target이 존재하면 해당 인덱스를 반환하고, 존재하지 않으면 "없음"이라는 문자열을 반환하는
 반복문 기반 이진 탐색 함수를 작성하시오.

'''


from typing import List, Union
# def binary_search(nums: List[int], target: int) -> Union[int, str]:
def binary_search(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if nums[mid] == target:
        return mid
    else:
        return '없음'


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# target = 4
target = 0
print(binary_search(nums, target))


