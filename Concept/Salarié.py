class Salarié(object):

    def __init__(self,nom,prenom):
        print("Création d'un objet salarié")
        #self.Nom=nom ## attributs public utilisable par tout le monde
        #self._Nom=nom ## attributs protégé (utilisable par l'héritage)
        #self.__Nom=nom ## attributs privé (non utilisable par l'héritage)
        self.__Nom=nom
        self.__Prenom=prenom
    
    def get_nom(self):
        return self.__Nom
    
    def get_prenom(self):
        return self.__Prenom
    
    def set_nom(self,nom):
        if type(nom)!=str or nom=="":
            print("Le nom doit être une chaine de caractères")
            
        else:
            self.__Nom=nom

    def set_prenom(self,prenom):
        if type(prenom)!=str or prenom=="":
            print("Le prénom doit être une chaine de caractères")
        else:
            self.__Prenom=prenom

    def afficher(self):
        print("Nom : ",self.__Nom)
        print("Prénom : ",self.__Prenom)

class User(Salarié):
    def __init__(self, nom, prenom, login, pwd):
        print("Création d'un objet User")
        #Salarié.__init__(self,nom,prenom)
        super().__init__(nom,prenom)
        self.Login=login
        self.Password=pwd
    # Les get et les set pour les attributs login et pwd

    def Afficher_User(self):
        self.afficher()
        print("User : ",self.get_nom(),"",self.get_prenom())

## Autres méthodes
# def GenPWD(self):
# def GenPWD():
# def hashPWD(self,pwd):
# def VerifyPWD(self, pwd):

# main programme principal

salarié1 = Salarié("OULMI","Céline")
salarié1.afficher()

