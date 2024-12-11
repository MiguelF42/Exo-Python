x=input("Ecrivez une phrase : ")

def nbr_mots(phrase):
    Dico = {}
    for i in phrase.lower().replace(",","").replace(".","").replace(";","").replace("!","").replace("?","").split(" "):
        if i in Dico:
            Dico[i] += 1
        else: 
            Dico[i] = 1
    return Dico

print(nbr_mots(x))