from math import sqrt, pi, log10
from functions import get_float

def liaison():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        print("1. Convertir en dB")
        print("2. Convertir en linéaire")
        print("3. Calculer Lp")
        print("4. Calculer dmax")
        print("5. ")
        print("6. Sortir")
        
        choice = input("Entrer votre choix: ")
        
        if choice == '1':
            convert_db()
        elif choice == '2':
            convert_lin()
        elif choice == '3':
            calcul_Lp()
        elif choice == '4':
            calcul_d()
        elif choice == '5':
            continue
        elif choice == '6':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1-6.")

def convert_db():
    """
    Convertit une puissance en dB.
    """
    P = get_float("Entrer la puissance P: ")
    print("La puissance en dB est: ", "{:.3e}".format(10*log10(P)))

def convert_lin():
    """
    Convertit une puissance en linéaire.
    """
    P = get_float("Entrer la puissance P: ")
    print("La puissance en linéaire est: ", "{:.3e}".format(10**(P/10)))

def calcul_Lp():
    """
    Calcule la perte en ligne Lp.
    """
    # Constante pour la vitesse de la lumière
    C = 3*(10**8)
    
    F = get_float("Entrer la fréquence F: ")
    d = get_float("Entrer la distance d: ")
    Lp = (4*pi*d*F/C)**2
    Lp_dB = 10*log10(Lp)
    print("La perte en ligne Lp est: ", "{:.3e}".format(Lp_dB), "dB")
    print("La perte en ligne Lp est: ", "{:.3e}".format(Lp), "W")

def calcul_d():
    """
    Calcule la distance dmax.
    """
    # Constante pour la vitesse de la lumière
    C = 3*(10**8)
    
    F = get_float("Entrer la fréquence F: ")
    Lp_type = input("La perte en ligne Lp est-elle en dB (1) ou en valeur linéaire (2) ? (1/2): ")
    if Lp_type == '1':
        Lp_db = get_float("Entrer la perte en ligne Lp en dB: ")
        Lp = 10**(Lp_db/10)  # Convertit dB en linéaire
    elif Lp_type == '2':
        Lp = get_float("Entrer la perte en ligne Lp en valeur linéaire: ")
    else:
        print("Entrée invalide. Veuillez entrer '1' pour dB ou '2' pour valeur linéaire.")
        return
    d = sqrt(Lp)*C/(4*pi*F)
    print("La distance dmax est: ", "{:.3e}".format(d), "m")
