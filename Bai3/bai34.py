n = int(input("Nhap so khoan chi: "))
expenses = []

for i in range(n):
    data = input().split(",")

    name = data[0].strip()
    price = int(data[1].strip())
    category = data[2].strip()

    expense = (name, price, category)
    expenses.append(expense)

print("\nDanh sach khoan chi:")
for expense in expenses:
    print(expense)

total = 0
for expense in expenses:
    total += expense[1]

print("\nTong chi tieu:", total, "VND")

# Thống kê theo danh mục
print("\nThong ke theo danh muc:")

categories = set()
for expense in expenses:
    categories.add(expense[2])

for category in categories:
    count = 0
    total_money = 0

    for expense in expenses:
        if expense[2] == category:
            count += 1
            total_money += expense[1]

    print(category)
    print("So khoan chi:", count)
    print("Tong so tien:", total_money, "VND")

if total > 5000000:
    print("Tong chi tieu vuot qua 5.000.000 VND")

max_expense = expenses[0]

for expense in expenses:
    if expense[1] > max_expense[1]:
        max_expense = expense

print("\nKhoan chi co so tien lon nhat:")
print(max_expense)