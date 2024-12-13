##############  Exemple d'une classe Mere et d'un cas d'héritage ###################
#############    By Céline OULMI  ###################

import Password
import Database

class Etudiant(object):  ## qui hérite de object
    """Classe des étudiants"""           # Documentation de la classe

### Constructeur de la classe : construite et initialiser un  objet
    def __init__(self, nom, pnom, nbEtud, specialite):
        print ("Création d'un objet étudiant...")
        #self._Nom=nom  ### attribut protégé (en protected, suite héritage, accessibles aux classes qui dérivent self.__Nom = nom  ### attribut privée ( lnaccessible de l'exterieur)
        #self.__Nom=nom  ## attribut privé, inaccessible de l'exterieur
        ### Sinon
        self.Nom=nom   ## 2 attributs Nom et Prenom en public, accessible à tous
        self.Prenom=pnom
        self.NbEtud=nbEtud
        self.Specialite=specialite
### Les méthodes getter et setter (sécurité d'accès) 
    def get_nom(self):  # Méthode 'get' pour retourner le nom
        return self.Nom
    def get_pnom(self):
        return self.Prenom
    def get_nbEtud(self):
        return self.NbEtud
    def get_specialite(self):
        return self.Specialite
  ### pour toutes les caratéristiques ou attributs de la classe
    def set_nom(self, nouveau_nom):   # Méthode 'set' pour modifier le nom
        if nouveau_nom == "":
            print ("Le nom de l'étudiant ne peut pas être vide!!!!")
        else:
            self.Nom = nouveau_nom
            print ("Le Nom à été modifié.") 
        User.updateUser(self)

    def set_pnom(self, nouveau_pnom):   # Méthode 'set' pour modifier le nom
        if nouveau_pnom == "":
            print ("Le prénom de l'employé ne peut pas être vide!!!!")
        else:
            self.Prenom = nouveau_pnom
            print ("Le Nom à été modifié.")
        User.updateUser(self)

    def set_nbEtud(self, nouveau_nbEtud):   # Méthode 'set' pour modifier le nom
        if nouveau_nbEtud == "":
            print ("Le nombre d'étudiants ne peut pas être vide!!!!")
        else:
            self.NbEtud = nouveau_nbEtud
            print ("Le nombre d'étudiants à été modifié.")
        User.updateUser(self)
    
    def set_specialite(self, nouvelle_specialite):   # Méthode 'set' pour modifier le nom
        if nouvelle_specialite == "":
            print ("La spécialité de l'étudiant ne peut pas être vide!!!!")
        else:
            self.Specialite = nouvelle_specialite
            print ("La spécialité à été modifiée.")
        User.updateUser(self)

### Autres méthode, exemple affichage            
    def afficher(self):
        print (self.Nom, " a été ajouté(e)")
        
### Création d'une nouvelle classe Users
### User est une classe qui hérite de la classe Salarié#

### Les attributs pour la classe User : Nom et Prenom hérités,
### puis Login et Password au moins
### classe User :
    
class User(Etudiant):
### constructeur de la nouvelle classe User
    def __init__(self, nom, pnom, nbEtud, specialite, login="", pwd="", isAdmin=False,id=0):
        print ("Création d'un objet User...")
        ##Salarié.__init__(self,nom, pnom)  #### ou bien faire référence par super()
        super().__init__(nom, pnom, nbEtud, specialite)
        ##self.Nom = nom
        ##self.Prenom=pnom
        if login == "":
            self.Login = self.GenLogin()
        else:
            self.Login = login
        if pwd == "":
            self.Password = self.hashPWD(self.GenPWD())
        else:
            self.Password = pwd
        self.isAdmin = isAdmin
        self.id = id

    def get_login(self):
        return self.Login
    
    def get_isAdmin(self):
        return self.isAdmin
    
    def set_login(self, login):
        self.Login = login
        User.updateUser(self)

    def set_pwd(self, pwd):
        self.Password = self.hashPWD(pwd)
        User.updateUser(self)

    def set_isAdmin(self, admin):
        self.isAdmin = admin
        User.updateUser(self)

    ### les get et les set pour les attributs login et pwd
    def userFromDB(login):
        user = Database.selectUser(login)
        self = User(user[4], user[3], user[5], user[6], user[1], user[2], user[7], user[0])
        return self

    def Afficher_User(self):
        print("User : ", self.get_nom(),"", self.get_pnom())

    def afficherUsers():
        users = Database.selectAllUsers()
        print("======== Liste des utilisateurs =========")
        for user in users:
            print(user)
        print("=========================================")

    def registerUser(user):
        Database.insertUser(user.get_nom(), user.get_pnom(), user.get_nbEtud(), user.get_specialite(), user.Login, user.Password)
        print("User enregistré")

    def updateUser(self):
        Database.updateUser(self.get_nom(), self.get_pnom(), self.get_nbEtud(), self.get_specialite(), self.Login, self.Password)
        print("User mis à jour")

    def deleteUser(self):
        Database.deleteUser(self.id)

    def GenLogin(self):
        print ("Génération d'un login")
        login = self.get_nom()[0] + self.get_pnom()
        print ("Login = ", login)
        return login

    def GenPWD(self):
        print ("Génération d'un mot de passe")
        pwd = Password.generate_password()
        print ("Mot de passe = ", pwd)
        return pwd

    def hashPWD(self, pwd, algo="sha256"):
        print ("Hashage du mot de passe")
        if algo == "sha256":
            return Password.hash_password_sha256(pwd)
        else:
            return Password.hash_password(pwd)
    
    def VerifPWD(self, pwd):
        print ("Vérification du mot de passe")
        if pwd.startswith("$2b$"):
            return Password.check_password(pwd, self.Password)
        else:
            return Password.check_password_sha256(pwd, self.Password)
        

## Fin classes donc de nouveaux types
        
### Autres méthodes    
##    def GenPWD(self):
##    def GenPWD():        
##    def hashPWD(self, pwd):
##    def VerifPWD(self), hashpwd):

    
### main, programme principal
## Classe mère : Salarié

# salarié1 = Salarié("OULMI","Céline")  # Initialiser un objet de la classe vide
# salarié1.afficher()               # Accéder à une méthode de la classe
 
# print ("Nom de l'employé est:", salarié1.get_nom()) # Accéder à une propriété de la classe
# print ("Modification du nom de la classe :")
# salarié1.set_nom("") # Génération d'une erreur, si Nom est vide
 
# salarié1.set_nom("Toto")
# salarié1.afficher()

# ## classe qui dérive : User
# User1=User("OULMI", "Céline", "coulmi", "Mypass")
# User1.Afficher_User()
# print("Nom de User&",User1.get_nom())


