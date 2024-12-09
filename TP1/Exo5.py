x=input("Ecrivez une phrase : ")

def nbr_mots(phrase):
    Dico = {}
    L = phrase.lower().replace(",","").split(" ")
    for i in L:
        if i in Dico:
            Dico[i] += 1
        else: 
            Dico[i] = 1
    return Dico

print(nbr_mots(x))
    