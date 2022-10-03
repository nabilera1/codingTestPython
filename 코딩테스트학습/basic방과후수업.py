# def Hello():
#     print('Hello ' * 5)
#
# Hello()

# myscore=list(map(int,input().split()))
# print(myscore)
# # myscore.sort()
# myscore=sorted(myscore,reverse=True)#내림차순 9 5 3 1 오름차순 1 3 5 9
# print(myscore[0])
# # 77 88 99 98
# cnt=0
# for i in range(1,101):
#     cnt+=str(i).count('3')
# print(cnt)
# for i in range(1,101,2):
#     print(i, end=' ')
#
mysum = lambda n: sum([int(x) for x in str(n)])
print("mysum():", mysum(111))