from math import sqrt

def equationDegre2(a,  b, c):
    delta=(b**2)-4*a*c
    if delta>0:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print("Il y a deux solutions dans les Réels: \n\tx1=",x1,"\n\tx2=",x2)
    elif delta==0:
        x=-b/(2*a)
        print("Il y a une solution dans les Réels: \n\t x=",x)    
    else:
        z1=(-b+1j*sqrt(-delta))/(2*a)
        z2=(-b-1j*sqrt(-delta))/(2*a)
        print("Il y a deux solutions complexes:\n\t z1=",z1,"\n\t z2=",z2)



a=float(input("Entrez le coeff' de x²: "))
b=float(input("Entrez le coeff' de x: "))
c=float(input("Entrez le coeff' constant: "))
equationDegre2(a,b,c)
