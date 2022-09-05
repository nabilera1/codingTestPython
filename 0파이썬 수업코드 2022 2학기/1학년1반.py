# txt = 'Life is short, ' \
#       'You need Python'
# print(txt)
# txt = "Life is short, " \
#       "You need Python"
# print(txt)
# txt = '''
# Life
# is
# short,
# You need Python
# '''
# print(txt)
# txt = """Life is short,
# You need Python"""
# print(txt)

#
# print('-' * 30)
# print('Korea  Japan  China')
# print('-' * 30)
#
# txt = 'Life is short, You need Python'
# print(len(txt)) # 길이를 리턴해주는 함수
#
# print(txt[0])
# print(txt[3])
# print(txt[29])
# print(txt[-1])
# print(txt[len(txt)-1]) # 30 - 1

# print('내가 좋아하는 음식은 %s 입니다.' % input("가장 좋아하는 음식은 무엇인가요? "))

pencil = int(input('연필의 판매 개수는?'))
eraser = int(input('지우개의 판매 개수는?'))
note = int(input('공책의 판매 개수는?'))
print('-'*30)
print("파이썬 문방구의 오늘 판매 내역")
print('-'*30)
print("%-7s : %4s 개, %6s원"% ("1. 연 필",pencil,pencil * 700))
print("%-7s : %4s 개, %6s원"% ("2. 지우개",eraser,eraser * 500))
print("%-7s : %4s 개, %6s원"% ("3. 노 트",note,note * 2500))