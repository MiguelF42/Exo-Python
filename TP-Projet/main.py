import Salarié

print('================Console Salarié===============')
print('')
print('1 pour se connecter')
print('2 pour créer un compte')
print('3 pour quitter')

choix = input('Votre choix : ')

UserList = []

while choix != '3':
    if choix == '1':
        print('Se connecter')
        login = input('Login : ')
        pwd = input('Password : ')
        logged = False
        for user in UserList:
            if user.Login == login:
                if user.VerifPWD(pwd):
                    print('Connecté')
                    Logged = True
                else:
                    print('Mot de passe incorrect')
                break
        if not Logged:
            print('Login incorrect')
    elif choix == '2':
        print('Créer un compte')
        nom = input('Nom : ')
        prenom = input('Prénom : ')
        login = input('Login : ')
        UserList.append(Salarié.User(nom, prenom, login))
        print('Compte créé')
    else:
        print('Choix invalide')
    print('')
    print('1 pour se connecter')
    print('2 pour créer un compte')
    print('3 pour quitter')
    choix = input('Votre choix : ')