# 학교 앞 문방구 주인의 오늘 매상은?

pencil = 0  # 연필
eraser = 0  # 지우개
notebook = 0  # 공책

# 단가
pencil_unit_price = 700
eraser_uint_price = 500
ntbook_unit_price = 2500

pencil = int(input('연필 판매 수량?'))
eraser = int(input('지우개 판매 수량?'))
notebook = int(input('공책 판매 수량?'))

n_pen = pencil * pencil_unit_price
n_era = eraser * eraser_uint_price
n_nt = notebook * ntbook_unit_price
sum = n_pen + n_era + n_nt
print('-' * 30)
print('파이썬 문방구의 오늘 매상')
print('-' * 30)
print('1. 연필 :', pencil, ', 매상 :', n_pen)
print('2. 지우개 :', eraser, ', 매상 :', n_era)
print('3. 공책 :', notebook, ', 매상 :', n_nt)
print('3. 공책 :', notebook, ', 매상 :', n_nt)
print('-' * 30)
print('오늘 총 판매액 : ',sum)
print('-' * 30)
