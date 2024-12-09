nom=input('Saisir nom : ')
prenom=input('Saisir prenom : ')
n=int(input('Saisir n : '))

if n%2==0:
    print(n,' est pair')
else:
    print(n,' est impair')

for i in nom:
    print(i)

for i in range(0,15,3):
    print(i)

for i in range(11):
    if i==8: continue
    if i==10: break
    print(i)

def ThereIsA(data):
    if 'a' in data:
        print('There is a')
    else:
        print('There is no a')

ThereIsA(nom)
ThereIsA(prenom)

def HowManyE(data):
    return data.count('e')

print(HowManyE(nom))
print(HowManyE(prenom))

def Carre(n):
    return n**2

print(Carre(n))

def Sum(a,b,c):
    return a+b+c

print(Sum(1,2,3))

# for i in range(1,1201):
#     print(i,'€ =',i*1.05,'$')

for i in range(1,8):
    print('*'*i)

