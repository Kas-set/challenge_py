
class Personne:
    def __init__(self, nom, prenom, age, lieuNaiss):
        self.nom = nom
        self.prenom = prenom
        self.age =age
        self.lieuNaiss = "|"+str(lieuNaiss)
    def show(self):
        print("Nom: " +self.nom + "\n" + "prenom: " + self.prenom + " age: " + str(self.age) +"\n|lieu de naissance: " +self.lieuNaiss)
        # print("preom: " + self.prenom)
        # print("age: " + str(self.age))
        # print("lieu de naissance: " +self.lieuNaiss)

Person_1 = Personne("kasa", "Godwin", 12, "Lomé")
# print(Person_1.nom)
chaine = Person_1.nom + Person_1.prenom + Person_1.lieuNaiss
print(chaine)
parties = chaine.split('|')
print(parties[1])
