import random

counter = 1

def print_consignes():
    global counter
    print("")
    print("=================Consigne n°"+str(counter)+"=================")
    print("")
    counter += 1

#==============================================================================
print_consignes()
#==============================================================================

length = int(input("Entrez un entier N supérieur ou égale à 20: "))

liste1 = [random.randint(1, 100) for i in range(length)] # Création de la liste, avec des entiers aléatoires entre 1 et 100

print("Liste 1 : ", liste1)

#==============================================================================
print_consignes()
#==============================================================================

length = int(input("Entrez un entier : ")) # Récupération des éléments entre les indices debut et fin
liste2 = []
i = 0
while len(liste2) < length:
    if liste1[i]%2 == 1:
        liste2.append(liste1[i])
    i += 1

print("Liste 2 : ", liste2)

#==============================================================================
print_consignes()
#==============================================================================

def display_reverse_sort(liste):
    liste.sort(reverse=True) # Tri décroissant
    print("Tableau trié : ", liste)

display_reverse_sort(liste1)
display_reverse_sort(liste2)

#==============================================================================
print_consignes()
#==============================================================================

def add_values(liste):
    val = int(input("Entrez une valeur à insérer dans le tableau 1 : "))
    place = input("Entrez la position où insérer la valeur (vide si à la fin) : ")

    if place == "": # Si la place est vide, on ajoute à la fin
        liste.append(val)
    else: # Sinon, on ajoute à la place indiquée
        liste.insert(int(place), val)

add_values(liste1)
print("Tableau 1 : ", liste1)

#==============================================================================
print_consignes()
#==============================================================================

def remove_val(liste):
    val = int(input("Entrez une valeur à supprimer de tableau 1 : "))
    c = liste.count(val) # On compte le nombre de fois que la valeur est présente
    for i in range(c): # On supprime toutes les occurences de la valeur
        liste.remove(val)

remove_val(liste1)
print("Tableau 1 : ", liste1)

#==============================================================================
print_consignes()
#==============================================================================

liste3 = []
for i in range(10):
    if i%2 == 0:
        liste3.append(liste1[random.randint(0, len(liste1)-1)]) # On ajoute un élément aléatoire de liste1 à liste3
    else:
        liste3.append(liste2[random.randint(0, len(liste2)-1)]) # On ajoute un élément aléatoire de liste2 à liste3
print("Tableau 3 : ", liste3)

#==============================================================================
print_consignes()
#==============================================================================

def reverse_list(liste):
    liste.reverse() # Inversion de la liste
    print("Tableau inversé : ", liste)

reverse_list(liste3)

#==============================================================================
print_consignes()
#==============================================================================

def pair_impair(liste1,liste2):
    pair = []
    impair = []
    for i in liste1:
        if i%2 == 0:
            pair.append(i)
    for i in liste2:
        if i%2 == 1:
            impair.append(i)
    return pair, impair

pair, impair = pair_impair(liste1, liste2)

print("Pair : ", pair)
print("Impair : ", impair)