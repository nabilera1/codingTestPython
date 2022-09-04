# n=list(input())
# print(n)
# a=list(map(int,n))
# nlist=list(input().split())
# iNum=[int(x) for x in nlist]
# print(sum(iNum))
# num = list(map(int, input().split()))
# print(sum(num))
# n1 = list(map(int, input().split()))
# print(n1)
# from collections import Counter
# num=[1,2,3]
# str=['one','two','three']
# result=dict(zip(str,num))
# print(result)
# print(result['one'])
# result=Counter(result)
# print(result.most_common(1))
from collections import Counter
print(Counter('abcdabcdababcdefefghi').most_common(3))

