from math import sqrt, pi, log10

# Constante pour la vitesse de la lumière
C = 3*(10**8)

def get_float(prompt):
    """
    Demande à l'utilisateur d'entrer un nombre flottant.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")

def get_positive_int(prompt):
    """
    Demande à l'utilisateur d'entrer un nombre entier positif.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("La valeur doit être un nombre entier positif. Veuillez réessayer.")
                continue
            return value
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")


def main():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        print("1. Convertir en dB")
        print("2. Convertir en linéaire")
        print("3. Calculer Lp")
        print("4. Calculer dmax")
        print("5. Calculer Feq")
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
            calcul_Feq()
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
    print("La puissance en dB est: ", 10*log10(P))

def convert_lin():
    """
    Convertit une puissance en linéaire.
    """
    P = get_float("Entrer la puissance P: ")
    print("La puissance en linéaire est: ", 10**(P/10))

def calcul_Lp():
    """
    Calcule la perte en ligne Lp.
    """
    F = get_float("Entrer la fréquence F: ")
    d = get_float("Entrer la distance d: ")
    Lp = (4*pi*d*F/C)**2
    Lp_dB = 10*log10(Lp)
    print("La perte en ligne Lp est: ", Lp_dB, "dB")
    print("La perte en ligne Lp est: ", Lp, "W")

def calcul_d():
    """
    Calcule la distance dmax.
    """
    F = get_float("Entrer la fréquence F: ")
    Lp_type = input("La perte en ligne Lp est-elle en dB (1) ou en valeur linéaire (2) ? (1/2): ")
    if Lp_type == '1':
        Lp_db = get_float("Entrer la perte en ligne Lp en dB: ")
        Lp = 10**(Lp_db/10)  # Convert dB to linear
    elif Lp_type == '2':
        Lp = get_float("Entrer la perte en ligne Lp en valeur linéaire: ")
    else:
        print("Entrée invalide. Veuillez entrer '1' pour dB ou '2' pour valeur linéaire.")
        return
    d = sqrt(Lp)*C/(4*pi*F)
    print("La distance dmax est: ", d, "m")

def calcul_Feq():
    """
    Calculate the equivalent noise factor Feq.
    """
    n = get_positive_int("Enter the number of quadrupoles n: ")
    F_type = input("Is the noise factor F in dB (1) or linear (2)? (1/2): ")

    # Initialize variables
    F, g, g_1 = 0, 0, 1

    for i in range(n):
        f = get_float(f"Enter the noise factor F{i+1}: ")

        # If F is in dB, convert it to linear
        if F_type == '1' and i != 0:
            f = 10**(f/10)

        # If not the first iteration, calculate F and g
        if i != 0:
            F += (f-1)/g
            g = get_float(f"Enter the gain G{i+1}: ")
            if F_type == '1':
                g = (10**(g/10))*g_1
            else:
                g *= g_1
            g_1 = g
        else:
            F = f if F_type == '2' else 10**(f/10)
            g = get_float(f"Enter the gain G{i+1}: ")

    # Print the equivalent noise factor
    if F_type == '1':
        Feq_db = 10*log10(F)
        print("The equivalent noise factor Feq is: ", Feq_db, "dB")
    elif F_type == '2':
        print("The equivalent noise factor Feq is: ", F)
    else:
        print("Invalid input. Please enter '1' for dB or '2' for linear value.")

if __name__ == "__main__":
    main()