class Personne:
    def __init__(self, nom:str):
        self.nom = nom 
    def sePresenter(self):
        print(f"Salut je m'appelle {self.nom}")
def demanderInfos():
    while True:
        try:
            nbr = int(input("Combien de personnes seront inscrits?: "))
            return nbr
        except:
            print("ERREUR:Saisir une valeur correcte!!!!!")

personnes = []
nbr = demanderInfos()
for i in range(nbr):
    nom = input(f"Saisir le nom de la personne {i+1}: ")
    personnes.append(Personne(nom))
for personne in personnes:
    personne.sePresenter()