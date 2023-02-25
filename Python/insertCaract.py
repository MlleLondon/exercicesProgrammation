def insertCaract(chaine, char):
    result=chaine[0]
    chaine=chaine[1:]
    for x in chaine:
        result=result+char+x
    print(result)

ch=input("Entrer une chaine de caractère: ")
n=input("Entrer la le caractère a imisser: ")
insertCaract(ch,n)