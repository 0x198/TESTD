import socket

# Configuration du client
SERVER_IP = '26.112.153.46'  # Remplacez par l'adresse IP publique du serveur
SERVER_PORT = 12345      # Le même port utilisé par le serveur

def connect_to_server():
    try:
        # Crée une socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connexion au serveur
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print(f"Connecté au serveur {SERVER_IP}:{SERVER_PORT}")
        
        # Recevoir le message du serveur
        welcome_message = client_socket.recv(1024).decode()
        print(f"Message du serveur : {welcome_message}")
        
        # Envoyer un message au serveur
        message = "Salut, serveur !"
        client_socket.sendall(message.encode())
        print("Message envoyé au serveur.")
        
    except Exception as e:
        print(f"Erreur : {e}")
        
    finally:
        # Fermer la connexion
        client_socket.close()
        print("Connexion fermée.")

if __name__ == "__main__":
    connect_to_server()
