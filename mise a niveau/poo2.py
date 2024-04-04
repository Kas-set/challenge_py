class Personne:
    def __init__(self, nom):
        self.nom = nom 
    def sePresenter(self):
        print(f"Salut je m'appelle {self.nom}")

nbr = int(input("Combien de personne seroent inscrit?: "))
personnes = []
for i in range(nbr):
    nom = input(f"Saisir le nom de la personne {i+1}: ")
    personnes.append(Personne(nom))
for personne in personnes:
    personne.sePresenter()