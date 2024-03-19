from math import log10
from functions import get_float, get_positive_int

def bruit():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        print("1. Calculer Feq")
        print("2. Calculer Teq")
        print("3. Sortir")
        
        choice = input("Entrer votre choix: ")
        
        if choice == '1':
            calcul_Feq()
        elif choice == '2':
            continue
        elif choice == '3':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1-3.")

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

def calcul_Teq():
    """
    Calcule la température de bruit équivalente Teq.
    """
    n = get_positive_int("Entrez le nombre de quadrupôles n: ")
    T_type = input("La température de bruit T est-elle en K (1) ou en dB (2)? (1/2): ")

    for i in range(n):
        t = get_float(f"Entrez la température de bruit T{i+1}: ")
        g = get_float(f"Entrez le gain G{i+1}: ")

        # Si T est en dB, la convertir en K
        if T_type == '2':
            t = 10**(t/10)

        # Calculer T et mettre à jour g_1
        if i == 0:
            T = t
            g_1 = g
        else:
            T += t/g_1
            g_1 *= g
        print("{:.3e}".format(T), "{:.3e}".format(g_1))

    # Imprimer la température de bruit équivalente
    if T_type == '2':
        Teq_db = 10*log10(T)
        print("La température de bruit équivalente Teq est: ", "{:.3e}".format(Teq_db), "dB")
    elif T_type == '1':
        print("La température de bruit équivalente Teq est: ", "{:.3e}".format(T))
    else:
        print("Entrée non valide. Veuillez entrer '1' pour K ou '2' pour la valeur en dB.")