input1 = input("Nhap so thich cua ban A:")
input2 = input("Nhap so thich cua ban B:")
listA = input1.split(",")
listB = input2.split(",")

for i in range(len(listA)):
    listA[i] = listA[i].strip().title()
for i in range(len(listB)):
    listB[i] = listB[i].strip().title()
setA = set(listA)
setB = set(listB)
print("So thich cua ban A:",setA)
print("So thich cua ban B:",setB)

same = setA and setB
if len(same) == 0:
    print("Khong co so thich chung")
else:
    print("So thich chung:",same)

onlyA = setA - setB
print("So thich chi ban A co:", onlyA)

all = setA | setB
print("Tat ca so thich cua hai ban:",all)

if len(all) == 0:
    similar = 0
else:
    similar = len(same) / len(all) *100
print(f"Do tuong dong:{similar :.2f}%")



