def Fic(Fichier): # Fonction qui prend en paramètre un fichier et retourne une liste des éléments du fichier
    Resultat = [ ]
    fichier=open(Fichier)
    while True :
        ligne = fichier.readline()
        if ligne == "" :
            break
        for mot in ligne.split() :
            if mot not in Resultat :
                Resultat.append(float(mot))
            else :
                Resultat.append(int(mot))
    fichier.close()
    return Resultat

print(Fic("fich.txt"))