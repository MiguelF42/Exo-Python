a=10
b=-2
if(a==10) &(b<2) :
    print("a et b corrects…")
############################# result: a et b corrects…
a=input("Entrez un nombre : ") ### exemple : a=-2
for i in range(12):
    print(i+1,a)
    a=a*3
############################# result[Pour a=-2]: 1 -2, 2 -6, 3 -18, 4 -54, 5 -162, 6 -486, 7 -1458, 8 -4374, 9 -13122, 10 -39366, 11 -118098, 12 -354294
for i in range(0,20):
    print(5*i)
############################# result: 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95
for i in range(10):
    print(" "+str(i)+"*6 = "+str(i*6))
############################# result: 0*6 = 0,  1*6 = 6,  2*6 = 12,  3*6 = 18,  4*6 = 24,  5*6 = 30,  6*6 = 36,  7*6 = 42,  8*6 = 48,  9*6 = 54
# Programme principal :
somme, nombreTotal, nombreGrands = 0, 0, 0
x = int(input("x (0 pour terminer) ?"))
while x > 0:
    somme += x
    nombreTotal += 1
    if x > 100:
        nombreGrands += 1
    x = int(input("x (0 pour terminer) ?"))
print("\nSomme :", somme)
print(nombreTotal, "valeur(s) en tout, dont", nombreGrands,"supérieure(s) à 100")
############################# result: le jeu continue tant que l'utilisateur entre un nombre positif, et affiche la somme des nombres entrés, le nombre total des nombres entrés et le nombre des nombres entrés supérieurs à 100