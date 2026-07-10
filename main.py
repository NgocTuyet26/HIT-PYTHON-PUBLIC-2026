ten = input("Nhập tên: ")
tuoi = int(input("Nhập tuổi: "))

if tuoi >= 18:
    print("Xin chào", ten, "- Bạn đã đủ 18 tuổi.")
else:
    print("Xin chào", ten, "- Bạn chưa đủ 18 tuổi.")

for i in range(1, 6):
    print(i)