from liaison import liaison
from bruit import bruit
from information import information

def main():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        print("1. Bilan de Liaison")
        print("2. Facteur de bruit")
        print("3. Théorie de l'information")
        print("4. Sortir")
        
        choice = input("Entrer votre choix: ")
        
        if choice == '1':
            liaison()
        elif choice == '2':
            bruit()
        elif choice == '3':
            information()
        elif choice == '4':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1-3.")

if __name__ == "__main__":
    main()