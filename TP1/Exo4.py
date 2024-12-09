Mylist1=[8, 4, 6, 10, 45, 23, 9, 10, 8]
Mylist2=[4.5, 2.0, 13.5, 2.5, 12.0]

print("Mylist1:", Mylist1)
print("Mylist2:", Mylist2)

Mylist3 = sorted(Mylist1)

print ("Mylist3:", Mylist3)

for i,j in enumerate(Mylist3):
    if Mylist3[i-1] == j: #Vérification de la présence d'un doublon
        Mylist3.pop(i) #Suppression du doublon

print("Mylist3:", Mylist3)

Mylist4 = sorted(Mylist1) + sorted(Mylist2)
print("Mylist4:", Mylist4)
index = Mylist4.index(4.5)
Mylist4.pop(index)
print("Mylist4:", Mylist4)
for i in Mylist3[::-1]:
    print(i)

for i in Mylist4[::-1]:
    print(i)