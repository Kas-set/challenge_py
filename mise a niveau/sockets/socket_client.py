import socket
import time

HOST_IP = "127.0.0.1" 
HOST_PORT = 3200
MAX_DATA_SIZE = 1024

print(f"Connexion au serveur {HOST_IP} au port {HOST_PORT}")
while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))
    except ConnectionRefusedError :
        print("ERROR: Impossilbe de se connecter au serveur.Reconnexion...")
        time.sleep(4)
    else:
        print("Connecté au serveur")
        break;

while True:
    data_recu = s.recv(MAX_DATA_SIZE)
    if not data_recu:
        break
    print("Message: ",data_recu.decode())
    texte_envoye = input("Vous: ")
    s.sendall(texte_envoye.encode())
# else:
#     print("Aucune Data")
s.close()
