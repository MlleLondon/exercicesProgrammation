def factoriel(n):
    p=1
    for i in range(1,n+1):
        p=p*i
    print(n,"!=",p)

n=int(input("Entrez un entier pour connaitre son factoriel: "))
factoriel(n)