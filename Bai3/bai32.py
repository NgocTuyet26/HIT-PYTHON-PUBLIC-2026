input1 = input("Nhap ten cac san pham: ")
input2 = input ("Nhap san pham can check: ")
products = input1.split(",")
print("Tong so san pham da mua:", len(products))

for i in range(len(products)):
    products[i] = products[i].strip().capitalize()

print("Danh sach san pham:")
print(products)

if len(products) % 2 != 0:
    center_products = products[len(products)//2]
    print("San pham o vi tri giua:", center_products)
else:
    print("Khong co san pham o vi tri giua")

count = 0
for product in set(products):
    if products.count(product) > count:
        count = products.count(product)
a =[]
for product in sorted(set(products)):
    if products.count(product) == count:
        a.append(product)
for product in a :
    print (product,"duoc mua nhieu nhat, so lan mua", count)


search = input2.strip().capitalize()
if search in products:
    print(search,"da duoc mua",products.count(search),"lan.")
else:
    print(search,"chua duoc mua")

products.insert(0,'Banh Nabati')

if 'Sua' in products:
    products.remove('Sua')

print("Danh sach sau khi cap nhat:",products)