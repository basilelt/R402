from math import sqrt, pi, log10
from functions import get_float
from bruit import calcul_Feq

def liaison():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        print("1. Convertir en dB")
        print("2. Convertir en linéaire")
        print("3. Calculer Lp")
        print("4. Calculer d")
        print("5. Calculer dmax")
        print("6. Calculer Pr")
        print("7. Calculer Pe")
        print("8. Diamètre antenne")
        print("9. Signal sur bruit")
        print("10. Calculer la sensibilité")
        print("11. Sortir")
        
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
            calcul_dmax()
        elif choice == '6':    
            calcul_Pr()
        elif choice == '7':
            calcul_Pe()
        elif choice == '8':    
            calcul_diamentre_antenne()
        elif choice == '9':
            calcul_signal_bruit()
        elif choice == '10':
            calcul_S()
        elif choice == '11':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1-10.")

def convert_db():
    """
    Convertit une puissance en dB.
    """
    P = get_float("Entrer la puissance P: ")
    print("La puissance en dB est: ", "{:.3e}".format(10*log10(P)), "dB")

def convert_lin():
    """
    Convertit une puissance en linéaire.
    """
    P = get_float("Entrer la puissance P: ")
    print("La puissance en linéaire est: ", "{:.3e}".format(10**(P/10)), "W")

def calcul_Lp(result_type=''):
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
    print("La perte en ligne linéaire Lp est: ", "{:.3e}".format(Lp))
   
    if result_type == '1':
        return Lp_dB
    elif result_type == '2':
        return Lp

def calcul_d(Lp=0):
    """
    Calcule la distance dmax.
    """
    # Constante pour la vitesse de la lumière
    C = 3*(10**8)
    F = get_float("Entrer la fréquence F: ")
    
    while Lp == 0:
        Lp_type = input("La perte en ligne Lp est-elle en dB (1) ou en valeur linéaire (2) ? (1/2): ")
        if Lp_type == '1':
            Lp_db = get_float("Entrer la perte en ligne Lp en dB: ")
            Lp = 10**(Lp_db/10)  # Convertit dB en linéaire
        elif Lp_type == '2':
            Lp = get_float("Entrer la perte en ligne Lp en valeur linéaire: ")
        else:
            print("Entrée invalide. Veuillez entrer '1' pour dB ou '2' pour valeur linéaire.")
            continue

    d = sqrt(Lp)*C/(4*pi*F)
    print("La distance d est: ", "{:.3e}".format(d), "m")
    
def calcul_dmax():
    """
    Calcule la distance dmax.
    """
    while True:
        unit = input("Voulez-vous entrer les valeurs en dB (1) ou en watts (2)? (1/2): ")
        if unit == '1':
            Gt = get_float("Entrer le gain de l'émetteur Gt en dB: ")
            Gr = get_float("Entrer le gain du récepteur Gr en dB: ")
            Pe = get_float("Entrer la puissance émise Pe en dB: ")
            S = get_float("Entrer la sensibilité S en dB: ")
            break
        elif unit == '2':
            Gt = 10*log10(get_float("Entrer le gain de l'émetteur Gt en watts: "))  # Convertit watts en dB
            Gr = 10*log10(get_float("Entrer le gain du récepteur Gr en watts: "))  # Convertit watts en dB
            Pe = 10*log10(get_float("Entrer la puissance émise Pe en watts: "))  # Convertit watts en dB
            S = 10*log10(get_float("Entrer la sensibilité S en watts: "))
            break
        else:
            print("Entrée non valide. Veuillez entrer '1' pour dB ou '2' pour watts.")

    Lpmax = S + Pe + Gt + Gr
    calcul_d(Lpmax)

def calcul_Pr():
    """
    Calcule la puissance reçue Pr.
    """
    while True:
        unit = input("Voulez-vous entrer les valeurs en dB (1) ou en watts (2)? (1/2): ")
        if unit == '1':
            Gt = get_float("Entrer le gain de l'émetteur Gt en dB: ")
            Gr = get_float("Entrer le gain du récepteur Gr en dB: ")
            Pe = get_float("Entrer la puissance émise Pe en dB: ")
            break
        elif unit == '2':
            Gt = 10*log10(get_float("Entrer le gain de l'émetteur Gt en watts: "))  # Convertit watts en dB
            Gr = 10*log10(get_float("Entrer le gain du récepteur Gr en watts: "))  # Convertit watts en dB
            Pe = 10*log10(get_float("Entrer la puissance émise Pe en watts: "))  # Convertit watts en dB
            break
        else:
            print("Entrée non valide. Veuillez entrer '1' pour dB ou '2' pour watts.")

    while True:
        Lp_known = input("La perte en ligne Lp est-elle connue ? Oui (1) ou non (2)? (1/2): ")
        if Lp_known == '1':
            if unit == '1':
                Lp = get_float("Entrer la perte en ligne Lp en dB: ")
            elif unit == '2':
                Lp = 10*log10(get_float("Entrer la perte en ligne Lp en watts: "))  # Convertit watts en dB
            break
        elif Lp_known == '2':
            Lp = calcul_Lp(unit)
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, la perte en ligne Lp est connue, ou '2' pour non.")
    Pr = Pe + Gt + Gr - Lp
    Pr_W = 10**(Pr/10)
    print("La puissance reçue Pr est: ", "{:.3e}".format(Pr), "dB")
    print("La puissance reçue Pr est: ", "{:.3e}".format(Pr_W), "W")
    return Pr_W
    
def calcul_Pe():
    """
    Calcule la puissance émise Pe.
    """
    while True:
        unit = input("Voulez-vous entrer les valeurs en dB (1) ou en watts (2)? (1/2): ")
        if unit == '1':
            Gt = get_float("Entrer le gain de l'émetteur Gt en dB: ")
            Gr = get_float("Entrer le gain du récepteur Gr en dB: ")
            Pr = get_float("Entrer la puissance reçue Pr en dB: ")
            break
        elif unit == '2':
            Gt = 10*log10(get_float("Entrer le gain de l'émetteur Gt en watts: "))  # Convertit watts en dB
            Gr = 10*log10(get_float("Entrer le gain du récepteur Gr en watts: "))  # Convertit watts en dB
            Pr = 10*log10(get_float("Entrer la puissance reçue Pr en watts: "))  # Convertit watts en dB
            break
        else:
            print("Entrée non valide. Veuillez entrer '1' pour dB ou '2' pour watts.")

    while True:
        Lp_known = input("La perte en ligne Lp est-elle connue ? Oui (1) ou non (2)? (1/2): ")
        if Lp_known == '1':
            if unit == '1':
                Lp = get_float("Entrer la perte en ligne Lp en dB: ")
            elif unit == '2':
                Lp = 10*log10(get_float("Entrer la perte en ligne Lp en watts: "))  # Convertit watts en dB
            break
        elif Lp_known == '2':
            Lp = calcul_Lp(unit)
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, la perte en ligne Lp est connue, ou '2' pour non, elle n'est pas connue.")

    Pe = Pr - Gt - Gr + Lp
    print("La puissance émise Pe est: ", "{:.3e}".format(Pe), "dB")
    print("La puissance émise Pe est: ", "{:.3e}".format(10**(Pe/10)), "W")

def calcul_diamentre_antenne():
    """
    Calcule le diamètre de l'antenne dm.
    """
    GdB = get_float("Entrer le gain de l'antenne en dB: ")
    FGHz = get_float("Entrer la fréquence F en GHz: ")
    dm = (10**((GdB-18)/20))/(FGHz)
    print("Le diamètre de l'antenne dm est: ", "{:.3e}".format(dm), "m")
    
def calcul_signal_bruit():
    """
    Calcule le rapport signal/bruit Eb/N0.
    """
    # Constante de Boltzmann
    k = 1.380649e-23

    Rb = get_float("Entrer le rythme binaire Rb (bit/s): ")
    T = get_float("Entrer la température T (K): ")

    # Calculer N0
    N0 = k * T

    # Calculer ou obtenir Pr
    while True:
        Pr_known = input("La puissance reçue Pr est-elle connue ? Oui (1) ou non (2)? (1/2): ")
        if Pr_known == '1':
            Pr = get_float("Entrer la puissance reçue Pr (W): ")
            break
        elif Pr_known == '2':
            Pr = calcul_Pr()
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, la puissance reçue Pr est connue, ou '2' pour non.")

    # Calculer Eb/N0
    Eb_N0 = Pr / (N0 * Rb)

    print("Le rapport signal/bruit Eb/N0 est: ", "{:.3e}".format(Eb_N0))
    print("Le rapport signal/bruit Eb/N0 est: ", "{:.3e}".format(10*log10(Eb_N0)), "dB")
    
def calcul_S():
    """
    Calcule la sensibilité S.
    """
    while True:
        Pr_known = input("La puissance reçue Pr est-elle connue ? Oui (1) ou non (2)? (1/2): ")
        if Pr_known == '1':
            Pr = get_float("Entrer la puissance reçue Pr (dB): ")
            break
        elif Pr_known == '2':
            Pr = 10*log10(calcul_Pr())
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, la puissance reçue Pr est connue, ou '2' pour non.")
    while True:
        Feq_known = input("Le facteur de bruit équivalent Feq est-il connu ? Oui (1) ou non (2)? (1/2): ")
        if Feq_known == '1':
            Feq = get_float("Entrer le facteur de bruit équivalent Feq (dB): ")
            break
        elif Feq_known == '2':
            Feq = calcul_Feq()
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, le facteur de bruit équivalent Feq est connu, ou '2' pour non.")
    print("La sensibilité est de: ", Pr+Feq, "dB")
