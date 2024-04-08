import socket
HOST_IP = "127.0.0.1" 
HOST_PORT = 3200
MAX_DATA_SIZE = 1024

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST_IP, HOST_PORT))
s.listen()



print(f"En attente de connexion sur {HOST_IP}, sur le port {HOST_PORT}....")
connection_socket, client_address = s.accept()
print(f"La connexion est etablie au {client_address}")

while True:
    texte_envoye = input("Vous: ")
    connection_socket.sendall(texte_envoye.encode())
    data_recu = connection_socket.recv(MAX_DATA_SIZE)
    if not data_recu:
        break
    print("Message: ", data_recu.decode())

s.close()
connection_socket.close()