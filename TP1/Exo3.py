list1='abc'
list2='de'

list3=[]

for i in list1:
    for j in list2:
        list3.append(i+j)

print(list3)