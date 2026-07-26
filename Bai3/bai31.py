a = input("Nhap chuoi:")
reverse = " "
for i in range(len(a)-1, -1, -1):
    reverse += a[i]
print ("Chuoi dao:", reverse)

sorted_string = sorted(a)
print("Chuoi sau khi sap xep:",sorted_string)

if a == reverse:
    print("Chuoi doi xung")
else:
    print("Chuoi khong doi xung")

characters = set(a)
count = 0
for c in characters:
    if a.count(c)> count:
        count = a.count(c)
b = []
for c in sorted(characters):
    if a.count(c) == count:
        b.append(c)
print("Ky tu xuat hien nhieu nhat: ",b, ",so lan xuat hien:", count)

lower_a = a.lower()
if 'u' in lower_a and 'e' in lower_a and 'o' in lower_a and 'a' in lower_a and 'i' in lower_a :
    print("Chuoi chua du 5 nguyen am")
else:
    print("Chuoi khong chua du 5 nguyen am")

