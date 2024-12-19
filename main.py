# import sys
# a = [1,2,3,4,5,6]
# b = a
# print(sys.getrefcount(a))
#
# a = int("256")
# b = int("256")
# print(a is b)




######### HOMEWORK ##################
# 30 masala
'''
k = int(input("Toplamlar sonini kiriting: "))
for i in range(k):
    print(f"{i + 1} toplam elementlarini kiriting (bosh joy bilan ajrating): ")
    collection = input().split()
    yigindi = 0
    for elem in collection:
        yigindi += int(elem)
    print(f"{i + 1}toplam yigindisi:", yigindi)
'''

# 31 masala
'''  
k = int(input("To'plamlar sonini kiriting: "))
soni = 0
for i in range(k):
    print(f"{i + 1} toplam elementlarini kiriting (bosh joy bilan ajrating): ")
    collection = input().split()
    mavjud = False
    for elem in collection:
        if int(elem) == 2:
            mavjud = True
            break
    if mavjud:
        soni += 1
print("2 soni bor bolgan toplamlar soni:", soni)
'''

# 32 masala
'''
k = int(input("Toplamlar sonini kiriting: "))
for i in range(k):
    print(f"{i + 1} toplam elementlarini kiriting (bosh joy bilan ajrating): ")
    collection = input().split()
    index = -1
    for j in range(len(collection)):
        if int(collection[j]) == 2:
            index = j
            break
    if index != -1:
        print(f"{i + 1} toplamdagi birinchi 2 sonining indeksi:", index)
    else:
        print(f"{i + 1} toplamda 2 yo‘q.")
'''

# 33 masala
'''
k = int(input("Toplamlar sonini kiriting: "))
for i in range(k):
    print(f"{i + 1} toplam elementlarini kiriting (bosh joy bilan ajrating): ")
    collection = input().split()
    index = -1
    for j in range(len(collection)):
        if int(collection[j]) == 2:
            index = j
    if index != -1:
        print(f"{i + 1} toplamdagi oxirgi 2 sonining indeksi:", index)
    else:
        print(f"{i + 1} toplamda 2 yoq.")
'''

# 34 masala
'''
k = int(input("Toplamlar sonini kiriting: "))
for i in range(k):
    print(f"{i + 1} toplam elementlarini kiriting (bosh joy bilan ajrating): ")
    collection = input().split()
    mavjud = False
    yigindi = 0
    for elem in collection:
        yigindi += int(elem)
        if int(elem) == 2:
            mavjud = True
    if mavjud:
        print(f"{i + 1} toplam yigindisi:", yigindi)
    else:
        print(f"{i + 1} toplamda 2 yoq, natija: 0")
'''

# 35 36 masala
'''
a = int(input("Toplam sonini kiriting:"))
i = 0
l = []

while a > i:
    i += 1
    r = []
    d = True
    while d:
        f = int(input("Son kiriting:"))
        if f == 0:
            d = False
        r.append(f)
    print(f"{i}-to'plam yaratildi.")
    l.append(r)
print([i[:-1] for i in l if sorted(i[:-1]) == i[:-1]])
'''

# 37 masala
'''
k = int(input("Toplamlar sonini kiriting: "))
javob = 0

for i in range(k):
    print(f"{i + 1}- toplam elementlarini kiriting (0 bilan tugating): ")
    collection = []
    while True:
        elem = int(input())
        if elem == 0:
            break
        collection.append(elem)

    if len(collection) >= 2:
        osuvchi = True
        kamayuvchi = True
        for j in range(len(collection) - 1):
            if collection[j] >= collection[j + 1]:
                osuvchi = False
            if collection[j] <= collection[j + 1]:
                kamayuvchi = False
        if osuvchi or kamayuvchi:
            javob += 1

print("Osuvchi yoki kamayuvchi toplamlar soni:", javob)
'''