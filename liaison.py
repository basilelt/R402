from math import sqrt, pi, log10

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

def liaison():
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

def calcul_Feq():
    """
    Calcule le facteur de bruit équivalent Feq.
    """
    n = get_positive_int("Entrez le nombre de quadrupôles n: ")
    F_type = input("Le facteur de bruit F est-il en dB (1) ou linéaire (2)? (1/2): ")

    for i in range(n):
        f = get_float(f"Entrez le facteur de bruit F{i+1}: ")
        g = get_float(f"Entrez le gain G{i+1}: ")

        # Si F et G sont en dB, les convertir en linéaire
        if F_type == '1':
            f = 10**(f/10)
            g = 10**(g/10)

        # Calculer F et mettre à jour g_1
        if i == 0:
            F = f
            g_1 = g
        else:
            F += (f-1)/g_1
            g_1 *= g
        print("{:.3e}".format(F), "{:.3e}".format(g_1))

    # Imprimer le facteur de bruit équivalent
    if F_type == '1':
        Feq_db = 10*log10(F)
        print("Le facteur de bruit équivalent Feq est: ", "{:.3e}".format(Feq_db), "dB")
    elif F_type == '2':
        print("Le facteur de bruit équivalent Feq est: ", "{:.3e}".format(F))
    else:
        print("Entrée non valide. Veuillez entrer '1' pour dB ou '2' pour la valeur linéaire.")