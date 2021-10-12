import itertools
#순서는 중요하고, 중복은 허용 안될때
arr=list(itertools.permutations(range(1,5),2))
print(arr)
# for i in arr:
#     print(i)
# https://wikidocs.net/23278
# 순서는 중요하고, 중복은 허용될때
arr=list(itertools.product([1,2,3,4,5],[1,2,3,4,5]))
print(arr)
# 순서는 중요하지 않고 순서 없이, 중복은 허용안될때
arr=list(itertools.combinations([1,2,3,4,5], 2))
print(arr)

