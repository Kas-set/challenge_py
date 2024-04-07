import json

personne={
    "nom":"kassa",
    "age":15,
    "amis":["joe","jack","avril"]
}
personne_json = json.dumps(personne)
print(personne_json)


# f = open("mon_fichierJson.txt", "w")
f = open("mon_fichierJson.txt", "r")
# f.write(personne_json)
donnees = f.read()
personneRecup = json.loads(donnees)
print(personneRecup)
f.close()