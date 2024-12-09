My_list=[17,20,38,26,68,45]
My_list = sorted(My_list) # Triage de la liste
print(My_list) # Affichage de la liste triée
My_list.append(17) # Ajout de 17 à la fin de la liste
print(My_list.count(17)) # Compte et affiche le nombre de 17 dans la liste
My_list = sorted(My_list,reverse=True) # Retriage de la liste de manière inversée
print(My_list) # Affichage de la liste triée à l'envers
print(len(My_list)) # Affichage du nombre d'éléments de la liste
index = My_list.index(38) # Affichage de l'index de 38 dans la liste
My_list.pop(index) # Suppression de l'élément 38 de la liste
print(My_list[2:4]) # Affichage de la sous liste allant du 3ème au 4ème élément de la liste
print(My_list[:2]) # Affichage de la sous liste allant du 1er au 2ème élément de la liste
print(My_list[2:]) # Affichage de la sous liste allant du 3ème élément jusqu'à la fin de la liste
print(My_list[-1]) # Affichage du dernier élément de la liste