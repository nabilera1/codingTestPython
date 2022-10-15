'''
list.sort() : list 원본이 바뀜(in-place), 리턴은 None
sorted(list) : list 원본은 그대로 두고 정렬된 리스트 값을 리턴
'''

nums = [1, 4, 3, 2]
print('1:', nums)
newNums = nums.sort()  # 원본을 정렬하고 수정(in-place)
print('-----정렬 후-----')
print('2:', nums)
print('3:', newNums)

nums1 = [1, 4, 3, 2]
print('\n1:', nums1)
newNums1 = sorted(nums1)  # 원본은 유지하고 정렬한 새 리스트에 복사
print('-----정렬 후-----')
print('2:', nums1)
print('3:', newNums1)

'''
sort(reverse=True) : 오름차순, 내림차순
reverse() : 순서 뒤집기
'''
nums = [1, 4, 3, 2]
print('\n1:', nums)
newNums = nums.sort(reverse=True)  # 원본을 정렬하고 수정(in-place)
print('-----내림 차순 정렬 후-----')
print('2:', nums)
print('3:', newNums)

nums = [1, 4, 3, 2]
print('\n1:', nums)
newNums = nums.reverse()  # 정렬이 아닌 뒤집기이고 수정(in-place)
print('-----reverse 후-----')
print('2:', nums)
print('3:', newNums)


# https://docs.python.org/ko/3/howto/sorting.html

print(sorted(nums, reverse=True))