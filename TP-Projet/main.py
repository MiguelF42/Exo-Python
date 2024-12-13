import Etudiant

print('================Console Etudiant===============')
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
        user = Etudiant.User.userFromDB(login)
        if not user or not user.VerifPWD(pwd):
            print('Login incorrect')
        else :
            if user.isAdmin:
                print('Connecté en tant qu\'admin')
            else:
                print('Connecté')
    else:
        print('Choix invalide')
    print('')
    print('1 pour se connecter')
    print('2 pour créer un compte')
    print('3 pour quitter')
    choix = input('Votre choix : ')
