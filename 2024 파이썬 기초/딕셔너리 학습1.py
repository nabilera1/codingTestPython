products = {
    "노트북": {"가격": 1000000, "재고": 10, "카테고리": "컴퓨터"},
    "스마트폰": {"가격": 800000, "재고": 20, "카테고리": "휴대폰"},
    "태블릿": {"가격": 500000, "재고": 15, "카테고리": "컴퓨터"},
    "카메라": {"가격": 300000, "재고": 5, "카테고리": "카메라"}
}

for k, v in products.items():
    print(k, v)

for k, v in products.items():
    print(v.keys(), v)
    for k1, v1 in v.items():
        print(k1, v1)

print("*" * 40)
# 카테고리별 재고 수량 계산
print('카테고리별 재고 수량 계산')
category_stock = {}

for product, info in products.items():
    category = info["카테고리"]
    stock = info["재고"]

    # if category in category_stock.keys():
    if category in category_stock:
        category_stock[category] += stock
    else:
        category_stock[category] = stock

# 결과 출력
# for category, total_stock in category_stock.items():
for category, total_stock in category_stock.items():
    print(f"{category}: {total_stock}개")

