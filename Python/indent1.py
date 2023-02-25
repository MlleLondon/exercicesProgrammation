def indent(x):
    if x>0:
        x=x+1
        y=0
        print("La fonction donne: ",x,y)
    del y

n=eval(input("Entrer un nombre: "))
indent(n)