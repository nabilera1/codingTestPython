
orders={
    'a1':50,
    'a2':46,
    'b1':89,
    'c1':67
}
sort_orders=sorted(orders.items(),key=lambda x:x[1],reverse=False)

print(sort_orders)
for i in sort_orders:
    print(i[0],i[1])
print()
sort_orders=sorted(orders.items(),key=lambda x:x[1],reverse=True)
#내림차순
for i in sort_orders:
    print(i[0],i[1])
