def nbOccurence(chaine, mot):
    nb=0
    for x in chaine:
        if x==mot:
            nb=nb+1
    print(mot," apparait ",nb," fois dans: ", chaine)

ch=input("Entrer une phrase, un mot: ")
n=input("Entrer la lettre à chercher: ")
nbOccurence(ch, n)