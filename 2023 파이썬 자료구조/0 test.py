# import sys
# sys.setrecursionlimit(10000)
#
# def getActualPalindrome(data, s, e, Link) :
#     print(s, e)
#     if s > e :
#         return ""
#     if s == e :
#         return data[s]
#     else :
#         if Link[s][e] == 1 :
#             return data[s] + getActualPalindrome(data, s+1, e-1, Link) + data[s]
#         elif Link[s][e] == 2 :
#             return getActualPalindrome(data, s+1, e, Link)
#         else :
#             return getActualPalindrome(data, s, e-1, Link)
#
# def getPalindrome(data) :
#     '''
#     문자열 data가 주어질 때, 이를 팰린드롬으로 만들기 위해 제거해야 하는 문자 개수의 최솟값을 반환하는 함수를 작성하세요.
#     '''
#
#     n = len(data)
#
#     Table = [ [ 0 for i in range(n) ] for j in range(n) ]
#     Link = [ [ 0 for i in range(n) ] for j in range(n) ]
#
#
#     for i in range(n-1, -1, -1) :
#         Table[i][i] = 0
#
#         for j in range(i+1, n) :
#             if data[i] == data[j] :
#                 Table[i][j] = Table[i+1][j-1]
#                 Link[i][j] = 1
#             else :
#                 if Table[i+1][j] < Table[i][j-1] :
#                     Link[i][j] = 2
#                 else :
#                     Link[i][j] = 3
#
#                 Table[i][j] = min(Table[i+1][j], Table[i][j-1]) + 1
#     return getActualPalindrome(data, 0, n-1, Link)
#
# def main():
#     '''
#     이 부분은 수정하지 마세요.
#     '''
#
#     s = input()
#
#     print(getPalindrome(s))
#
# if __name__ == "__main__":
#     main()

print([False]*5)
print([False] for _ in range(5))
print([[False] for _ in range(5)])
print('*' * 30)

print([0]*5)
print([0 for _ in range(5)])
print([0] for _ in range(5))
print([[0] for _ in range(5)])
print('*' * 30)

n = 4
graph = [ [ 0 for j in range(n) ] for i in range(n) ]
print(graph)

graph = [ [0] * 4 for _ in range(4)]
print(graph)

graph = [ 0 * 4 for _ in range(4)]
print(graph)

graph = [ '0' * 4 for _ in range(4)]
print(graph)