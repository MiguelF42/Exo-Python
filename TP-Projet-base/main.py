import Salarié

print('================Console Salarié===============')
print('')
print('1 pour se connecter')
print('2 pour créer un compte')
print('3 pour quitter')

choix = input('Votre choix : ')

while choix != '3':
    if choix == '1':
        print('Se connecter')
        login = input('Login : ')
        pwd = input('Password : ')
        user = Salarié.User.userFromDB(login)
        if user and user.VerifPWD(pwd):
            print('Connecté')
            continue
        else :
            print('Login incorrect')
    elif choix == '2':
        print('Créer un compte')
        nom = input('Nom : ')
        prenom = input('Prénom : ')
        login = input('Login : ')
        Salarié.User(nom, prenom, login).registerUser()
        print('Compte créé')
    else:
        print('Choix invalide')
    print('')
    print('1 pour se connecter')
    print('2 pour créer un compte')
    print('3 pour quitter')
    choix = input('Votre choix : ')
