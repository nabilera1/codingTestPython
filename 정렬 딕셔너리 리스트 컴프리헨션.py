#
# orders={
#     'a1':50,
#     'a2':46,
#     'b1':89,
#     'c1':67
# }
# sort_orders=sorted(orders.items(),key=lambda x:x[1])
# [print(key,value) for (key,value) in sort_orders]


orders={
    'bts햄버거':90,
    '기본버거':46,
    '소고기버거':89,
    '참치버거':67
}
sort_orders=sorted(orders.items(),key=lambda x:x[1])
[print(key,value) for (key,value) in sort_orders]