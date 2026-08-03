#BAI 3
# def nhap(n, list_number):
#     for i in range(n):
#         x = int(input(f"Nhap so thu {i + 1}:"))
#         list_number.append(x)
# def chan_le(list_number):
#     chan = 0
#     le = 0
#     for x in list_number:
#         if x % 2 == 0:
#             chan += 1
#         else :
#             le += 1
#     return  chan, le
       
# def tong(list_number):
#     sum = 0
#     for x in list_number:
#         sum += x
#     return sum

# def sap_xep(list_number):
#     new_list = list_number.copy()
#     new_list.sort()
#     return new_list
# n = int(input("Nhap so luong phan tu:"))
# numbers = []
# nhap(n,numbers)
# print("Day so:", numbers)
# chan,le = chan_le(numbers)
# print("So luong phan tu chan:",chan)
# print("So luong phan lẻ:",le)
# print("Tong:",tong(numbers))
# print("Day so sau khi sap xep",sap_xep(numbers) )

#BAI 2
# def gcd(a,b):
#     if b == 0:
#         return a
#     return gcd(a,a%b)
# def gcd(a,b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
# a = int(input("Nhap so nguyen a:"))
# b = int(input("Nhap so nguyen b:"))

# print("UCLN = ",gcd(a,b))

# isEven = lambda x : x % 2 == 0
# print(isEven(5))
# print(isEven(8))
# sum = lambda a,b : a + b
# print(sum(5,6))

# BAI 4
# nums = [ 1,2,3,4,5]
# new_nums =[]
# new_nums = list(filter(lambda x : x % 2 == 0,nums))
# print(new_nums)

# new1_nums = []
# new1_nums = list(map(lambda x : x**2,new_nums))
# print(new1_nums)

# dictionary = {}

# while True:
#     print("1. Thêm từ vựng mới")
#     print("2. Tra cứu ý nghĩa")
#     print("3. Cập nhật ý nghĩa")
#     print("4. Xóa một từ vựng")
#     print("5. Xóa toàn bộ từ điển")
#     print("6. In ra toàn bộ từ vựng")
#     print("7. In ra toàn bộ từ điển")
#     print("8. Kết thúc")

#     choice = int(input("Nhập lựa chọn: "))

#     if choice == 1:
#         word = input("Nhập từ vựng: ")
#         meaning = input("Nhập ý nghĩa: ")

#         if word in dictionary:
#             print("Từ vựng đã tồn tại!")
#         else:
#             dictionary[word] = meaning
#             print("Thêm thành công!")

#     elif choice == 2:
#         word = input("Nhập từ cần tra: ")

#         if word in dictionary:
#             print("Ý nghĩa:", dictionary[word])
#         else:
#             print("Không tìm thấy từ vựng!")

#     elif choice == 3:
#         word = input("Nhập từ cần cập nhật: ")

#         if word in dictionary:
#             meaning = input("Nhập ý nghĩa mới: ")
#             dictionary[word] = meaning
#             print("Cập nhật thành công!")
#         else:
#             print("Không tìm thấy từ vựng!")

#     elif choice == 4:
#         word = input("Nhập từ cần xóa: ")

#         if word in dictionary:
#             dictionary.pop(word)
#             print("Đã xóa!")
#         else:
#             print("Không tìm thấy từ vựng!")

#     elif choice == 5:
#         dictionary.clear()
#         print("Đã xóa toàn bộ từ điển!")

#     elif choice == 6:
#         if len(dictionary) == 0:
#             print("Từ điển rỗng!")
#         else:
#             print("Danh sách từ vựng:")
#             for word in dictionary.keys():
#                 print(word)

#     elif choice == 7:
#         if len(dictionary) == 0:
#             print("Từ điển rỗng!")
#         else:
#             print("Toàn bộ từ điển:")
#             for word, meaning in dictionary.items():
#                 print(f'"{word}" : "{meaning}"')

#     elif choice == 8:
#         print("Kết thúc chương trình!")
#         break

#     else:
#         print("Lựa chọn không hợp lệ!")