# nom = input("Quel est ton nom?")
# print(nom)
# print('Votre nom est '+ nom)
# print(f'Votre nom est {nom}')

# while 1==1:
#     print('hello')
import random
nombre_aleatoire = random.randint(1,5)
nombre_de_vie = 3
nombre_saisi = 0

while nombre_saisi != nombre_aleatoire:
    if(nombre_de_vie !=0):
        print("Vous avez " + str(nombre_de_vie) +" Vies")
        
        nombre_saisi_str = input("Saisir le nombre magique: ")
        
        try:
            nombre_saisi = int(nombre_saisi_str)
        except:
            print("Veuillez saisir un nombre valide")
        else:
            
            if(nombre_saisi != nombre_aleatoire):
                print("Mauvaise réponse !!")
                nombre_de_vie -=1
            else:
                print("Bonne Réponse")
    else:
        print("Désolé vous êtes mort !! Mais le nombre etait "+ str(nombre_aleatoire))
        break 

# nombre_saisi_str = input("Saisir le nombre magique: ")
      
# try:
#     nombre_saisi = int(nombre_saisi_str)
# except:
#     print("Veuillez saisir un nombre valide")