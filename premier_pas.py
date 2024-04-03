from turtle import all  
def Bonjour ():
    print("Bonjour tout le monde!")
Bonjour()
def Bonjour2(nom):
    print(f"Bonjour  {nom}!")
nom=input("Saisir un nom: ")
nbr=int(input("Vous voulez etre saluer combien de fois?: "))
for i in range(nbr):
    Bonjour2(nom)

liste=["kassa", "godwin","gladstone"]
def appel (liste_0):
    for i in range(len(liste_0)):
        print(f"Bonjour {liste_0[i]}")
appel(liste)
