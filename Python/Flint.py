def flint(a):
    if type(a)==int:
        print(a," est un entier !")
    else:
        print(a," est un flottant !")
    
n=eval(input("Entrer un nombre: "))
flint(n)