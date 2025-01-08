import os
import subprocess

def check_connected_devices():
    """
    Vérifie si un PC Windows est connecté via ADB.
    """
    try:
        # Vérifie les appareils connectés
        devices_output = subprocess.check_output(['adb', 'devices'], stderr=subprocess.STDOUT)
        devices = devices_output.decode().split('\n')
        
        # Filtrer les appareils listés
        connected_devices = [line for line in devices if 'device' in line and not line.startswith('List')]
        
        if connected_devices:
            print("Un appareil est connecté via ADB.")
            return True
        else:
            print("Aucun appareil connecté.")
            return False

    except Exception as e:
        print(f"Erreur lors de la vérification des appareils : {e}")
        return False

def execute_windows_command():
    """
    Exécute des commandes sur le PC Windows pour lancer Notepad et afficher 'BONJOUR'.
    """
    try:
        # Commande pour lancer Notepad
        launch_notepad = 'start notepad'
        # Commande pour envoyer un texte (automatisation simulée)
        send_text = 'echo BONJOUR'

        # Envoyer les commandes via ADB shell
        subprocess.run(['adb', 'shell', launch_notepad], check=True)
        subprocess.run(['adb', 'shell', send_text], check=True)

        print("Commande exécutée avec succès.")

    except Exception as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")

if __name__ == "__main__":
    if check_connected_devices():
        execute_windows_command()
    else:
        print("Assurez-vous que le téléphone est connecté à un PC Windows avec ADB activé.")
