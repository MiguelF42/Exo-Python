list1=["Vendredi",14,"Novembre"] # Création et initialisation de list1
print(list1) # Affichage de list1
print(list1[0]) # Affichage du premier élément de list1
print(len(list1)) # retourne le nombre d'éléments de list1
list1.append(2023) # Ajout de 2023 à la fin de list1
print(list1) # Affichage de list1
list1[3]+1 # Ajoute un au 4ème élément de list1
del list1[0] # Supprime le premier élément de list1
print(list1) # Affichage de list1
list1.insert(20,"Samedi") # Ajoute "Samedi" à la position 20 de list1
print(list1) # Affichage de list1
print("jeudi" in list1) # Affiche True si jeudi existe dans list1, False sinon
print("Samedi" in list1) # Affiche True si Samedi existe dans list1, False sinon
list2=list1[1:3] # Crée une liste contenant les éléments 2 et 3 de list1
print(list2) # Affichage de list2
list3=list1[:2] # Crée une liste d'éléments contenant les éléments 1 et 2 de list1
list4=list1[1:] # Crée une liste contenant tous les éléments de list1 sauf le 1er
print(list3) # Affichage de list3
print(list4) # Affichage de list4
list3=list3+[2021] # Ajoute 2021 à la fin de list3
print(list3) # Affichage de list3
list5=5*list1 # Crée une liste contenant 5 fois les éléments de list1
print(list5) # Affichage de list5
list1.extend([3,4]) # Ajoute 3 et 4 à la fin de list1
print(list1) # Affichage de list1
list6=list1.pop(0) # Supprime le premier élément de list1 et le stocke dans list6
print(list6) # Affichage de list6