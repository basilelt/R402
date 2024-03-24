from math import sqrt, pi, log10, log2
import matplotlib.pyplot as plt

def get_float(prompt):
    """
    Demande à l'utilisateur d'entrer un nombre flottant.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Entrée invalide. Veuillez\n"
                  "entrer un nombre.")

def get_positive_int(prompt):
    """
    Demande à l'utilisateur d'entrer un nombre entier positif.
    """
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("La valeur doit être un\n"
                      "nombre entier positif.\n"
                      "Veuillez réessayer.")
                continue
            return value
        except ValueError:
            print("Entrée invalide. Veuillez\n"
                  "entrer un nombre entier.")

################################################################################

def liaison():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        input("Appuyez sur entrer pour\n"
              "continuer")
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
        
        choice = input("Entrer votre choix:")
        
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
            calcul_diametre_antenne()
        elif choice == '9':
            calcul_signal_bruit()
        elif choice == '10':
            calcul_S()
        elif choice == '11':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez\n"
                  "entrer un chiffre entre 1-10.")
def convert_db():
    """
    Convertit une puissance en dB.
    """
    P = get_float("Entrer la puissance P:\n")
    print("La puissance en dB est:\n",
          "{:.3e}".format(10*log10(P)), "dB")

def convert_lin():
    """
    Convertit une puissance en linéaire.
    """
    P = get_float("Entrer la puissance\n"
                  "P (linéaire):\n")
    print("La puissance en linéaire est:\n",
          "{:.3e}".format(10**(P/10)), "W")

def calcul_Lp(result_type=''):
    """
    Calcule la perte en ligne Lp.
    """
    # Constante pour la vitesse de la lumière
    C = 3*(10**8)
    
    F = get_float("Entrer la fréquence F:\n")
    d = get_float("Entrer la distance d:\n")
    Lp = (4*pi*d*F/C)**2
    Lp_dB = 10*log10(Lp)
    print("La perte en ligne Lp est:\n",
          "{:.3e}".format(Lp_dB), "dB")
    print("La perte en ligne linéaire Lp est:\n",
          "{:.3e}".format(Lp))
    input("Appuyez sur entrer pour\n"
          "continuer")
   
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
    F = get_float("Entrer la fréquence F:\n")
    
    while Lp == 0:
        Lp_type = input("La perte en ligne Lp est\n"
                        "elle en dB (1) ou en valeur\n"
                        "linéaire (2) ? (1/2): ")
        if Lp_type == '1':
            Lp_db = get_float("Entrer la perte en ligne\n"
                              "Lp en dB:\n")
            Lp = 10**(Lp_db/10)  # Convertit dB en linéaire
        elif Lp_type == '2':
            Lp = get_float("Entrer la perte en ligne\n"
                           "Lp en valeur linéaire:\n")
        else:
            print("Entrée invalide. Veuillez\n"
                  "entrer '1' pour dB ou '2'\n"
                  "pour valeur linéaire.")
            continue

    d = sqrt(Lp)*C/(4*pi*F)
    print("La distance d est:\n",
          "{:.3e}".format(d), "m")
    
def calcul_dmax():
    """
    Calcule la distance dmax.
    """
    while True:
        unit = input("Voulez-vous entrer les\n"
                     "valeurs en dB (1) ou en\n"
                     "watts (2)? (1/2): ")
        if unit == '1':
            Gt = get_float("Entrer le gain de\n"
                           "l'émetteur Gt en dB:\n")
            Gr = get_float("Entrer le gain du\n"
                           "récepteur Gr en dB:\n")
            Pe = get_float("Entrer la puissance\n"
                           "émise Pe en dB:\n")
            S  = get_float("Entrer la sensibilité\n"
                          "S en dB:\n")
            break
        elif unit == '2':
            Gt = 10*log10(get_float("Entrer le gain de\n"
                                    "l'émetteur Gt en watts:\n"))  
            # Convertit watts en dB

            Gr = 10*log10(get_float("Entrer le gain du\n"
                                    "récepteur Gr en watts:\n"))  
            # Convertit watts en dB

            Pe = 10*log10(get_float("Entrer la puissance\n"
                                    "émise Pe en watts:\n"))  
            # Convertit watts en dB

            S = 10*log10(get_float("Entrer la sensibilité\n"
                                   "S en watts:\n"))  
            # Convertit watts en dB
            break
        else:
            print("Entrée non valide. Veuillez\n"
                  "entrer '1' pour dB ou '2'\n"
                  "pour watts.")

    Lpmax = S + Pe + Gt + Gr
    calcul_d(Lpmax)

def calcul_Pr():
    """
    Calcule la puissance reçue Pr.
    """
    while True:
        unit = input("Voulez-vous entrer les\n"
                     "valeurs en dB (1) ou en\n"
                     "watts (2)? (1/2): ")
        if unit == '1':
            Gt = get_float("Entrer le gain de\n"
                           "l'émetteur Gt en dB:\n")
            Gr = get_float("Entrer le gain du\n"
                           "récepteur Gr en dB: ")
            Pe = get_float("Entrer la puissance\n"
                           "émise Pe en dB:\n")
            break
        elif unit == '2':
            Gt = 10*log10(get_float("Entrer le gain de\n"
                                    "l'émetteur Gt en watts:\n"))  
            # Convertit watts en dB

            Gr = 10*log10(get_float("Entrer le gain du\n"
                                    "récepteur Gr en watts:\n"))  
            # Convertit watts en dB

            Pe = 10*log10(get_float("Entrer la puissance\n"
                                    "émise Pe en watts:\n"))  
            # Convertit watts en dB
            break
        else:
            print("Entrée non valide. Veuillez\n"
                  "entrer '1' pour dB ou '2'\n"
                  "pour watts.")

    while True:
        Lp_known = input("La perte en ligne Lp\n"
                         "est-elle connue ? Oui (1)\n"
                         "ou non (2)? (1/2): ")
        if Lp_known == '1':
            if unit == '1':
                Lp = get_float("Entrer la perte en ligne\n"
                               "Lp en dB:\n")
            elif unit == '2':
                Lp = 10*log10(get_float("Entrer la perte en\n"
                                        "ligne Lp en watts:\n"))  
                # Convertit watts en dB
            break
        elif Lp_known == '2':
            Lp = calcul_Lp(unit)
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, la\n"
                  "perte en ligne Lp est\n"
                  "connue, ou '2' pour non.")
    Pr = Pe + Gt + Gr - Lp
    Pr_W = 10**(Pr/10)
    print("La puissance reçue Pr est:\n",
          "{:.3e}".format(Pr), "dB")
    print("La puissance reçue Pr est:\n",
          "{:.3e}".format(Pr_W), "W")
    return Pr_W
    
def calcul_Pe():
    """
    Calcule la puissance émise Pe.
    """
    while True:
        unit = input("Voulez-vous entrer les\n"
                     "valeurs en dB (1) ou en\n"
                     "watts (2)? (1/2): ")
        if unit == '1':
            Gt = get_float("Entrer le gain de\n"
                           "l'émetteur Gt en dB: ")
            Gr = get_float("Entrer le gain du\n"
                           "récepteur Gr en dB: ")
            Pr = get_float("Entrer la puissance\n"
                           "reçue Pr en dB: ")
            break
        elif unit == '2':
            Gt = 10*log10(get_float("Entrer le gain de\n"
                                    "l'émetteur Gt en watts: "))  
            # Convertit watts en dB

            Gr = 10*log10(get_float("Entrer le gain du\n"
                                    "récepteur Gr en watts: "))  
            # Convertit watts en dB

            Pr = 10*log10(get_float("Entrer la puissance\n"
                                    "reçue Pr en watts: "))  
            # Convertit watts en dB
            break
        else:
            print("Entrée non valide. Veuillez\n"
                  "entrer '1' pour dB ou '2'\n"
                  "pour watts.")

    while True:
        Lp_known = input("La perte en ligne Lp\n"
                         "est-elle connue ? Oui (1)\n"
                         "ou non (2)? (1/2): ")
        if Lp_known == '1':
            if unit == '1':
                Lp = get_float("Entrer la perte en ligne\n"
                               "Lp en dB:\n")
            elif unit == '2':
                Lp = 10*log10(get_float("Entrer la perte en\n"
                                        "ligne Lp en watts:\n"))  
                # Convertit watts en dB
            break
        elif Lp_known == '2':
            Lp = calcul_Lp(unit)
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, la\n"
                  "perte en ligne Lp est\n"
                  "connue, ou '2' pour non.")

    Pe = Pr - Gt - Gr + Lp
    print("La puissance émise Pe est:\n",
          "{:.3e}".format(Pe), "dB")
    print("La puissance émise Pe est:\n",
          "{:.3e}".format(10**(Pe/10)), "W")

def calcul_diametre_antenne():
    """
    Calcule le diamètre de l'antenne dm.
    """
    GdB = get_float("Entrer le gain de\n"
                    "l'antenne en dB:\n")
    FGHz = get_float("Entrer la fréquence\n"
                     "F en GHz:\n")
    dm = (10**((GdB-18)/20))/(FGHz)
    print("Le diamètre de l'antenne\n"
          "dm est:\n",
          "{:.3e}".format(dm), "m")
    
def calcul_signal_bruit():
    """
    Calcule le rapport signal/bruit Eb/N0.
    """
    # Constante de Boltzmann
    k = 1.380649e-23

    Rb = get_float("Entrer le rythme binaire\n"
                   "Rb (bit/s):\n")
    T = get_float("Entrer la température\n"
                  "T (K):\n")

    # Calculer N0
    N0 = k * T

    # Calculer ou obtenir Pr
    while True:
        Pr_known = input("La puissance reçue Pr\n"
                         "est-elle connue ? Oui (1)\n"
                         "ou non (2)? (1/2): ")
        if Pr_known == '1':
            Pr = get_float("Entrer la puissance\n"
                           "reçue Pr (W):\n")
            break
        elif Pr_known == '2':
            Pr = calcul_Pr()
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, la\n"
                  "puissance reçue Pr est\n"
                  "connue, ou '2' pour non.")

    # Calculer Eb/N0
    Eb_N0 = Pr / (N0 * Rb)

    print("Le rapport signal/bruit\n"
          "Eb/N0 est:\n",
          "{:.3e}".format(Eb_N0))
    print("Le rapport signal/bruit\n"
          "Eb/N0 est:\n",
          "{:.3e}".format(10*log10(Eb_N0)), "dB")
    
def calcul_S():
    """
    Calcule la sensibilité S.
    """
    while True:
        Pr_known = input("La puissance reçue Pr\n"
                         "est-elle connue ? Oui (1)\n"
                         "ou non (2)? (1/2): ")
        if Pr_known == '1':
            Pr = get_float("Entrer la puissance\n"
                           "reçue Pr (dB):\n")
            break
        elif Pr_known == '2':
            Pr = 10*log10(calcul_Pr())
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, la\n"
                  "puissance reçue Pr est\n"
                  "connue, ou '2' pour non.")
    while True:
        Feq_known = input("Le facteur de bruit\n"
                          "équivalent Feq est-il\n"
                          "connu ? Oui (1) ou non\n"
                          "(2)? (1/2): ")
        if Feq_known == '1':
            Feq = get_float("Entrer le facteur de\n"
                            "bruit équivalent Feq (dB):\n")
            break
        elif Feq_known == '2':
            Feq = calcul_Feq()
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, le\n"
                  "facteur de bruit équivalent\n"
                  "Feq est connu, ou '2' pour non.")
    print("La sensibilité est de:\n",
          Pr+Feq, "dB")

################################################################################


def bruit():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        input("Appuyez sur entrer pour\n"
              "continuer")
        print("1. Calculer Feq")
        print("2. Calculer Teq")
        print("3. Sortir")
        
        choice = input("Entrer votre choix: ")
        
        if choice == '1':
            calcul_Feq()
        elif choice == '2':
            calcul_Teq()
        elif choice == '3':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez\n"
                  "entrer un chiffre entre 1-3.")

def calcul_Feq():
    """
    Calcule le facteur de bruit équivalent Feq.
    """
    n = get_positive_int("Entrez le nombre de\n"
                         "quadrupôles n: ")
    while True:
        F_type = input("Le facteur de bruit F\n"
                       "est-il en dB (1) ou\n"
                       "linéaire (2)? (1/2): ")
        if F_type not in ['1', '2']:
            print("Entrée non valide. Veuillez\n"
                  "entrer '1' pour dB ou '2'\n"
                  "pour la valeur linéaire.")
        else:
            break
    for i in range(n):
        f = get_float("Entrez le facteur de\n"
                      "bruit F{}:\n".format(i+1))
        g = get_float("Entrez le gain G{}:\n".format(i+1))

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

    # Imprimer le facteur de bruit équivalent
    if F_type == '1':
        Feq_db = 10*log10(F)
        print("Le facteur de bruit\n"
              "équivalent Feq est:\n",
              "{:.3e}".format(Feq_db), "dB")
    elif F_type == '2':
        print("Le facteur de bruit\n"
              "équivalent Feq est:\n",
              "{:.3e}".format(F))
        return Feq_db

def calcul_Teq():
    """
    Calcule la température de bruit équivalente Teq.
    """
    n = get_positive_int("Entrez le nombre de\n"
                         "quadrupôles n: ")
    while True:
        T_type = input("La température de bruit\n"
                       "T est-elle en K (1) ou\n"
                       "en dB (2)? (1/2): ")
        if T_type not in ['1', '2']:
            print("Entrée non valide. Veuillez\n"
                  "entrer '1' pour K ou '2'\n"
                  "pour la valeur en dB.")
        else:
            break

    for i in range(n):
        t = get_float("Entrez la température\n"
                      "de bruit T{}:\n".format(i+1))
        g = get_float("Entrez le gain G{}:\n".format(i+1))

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

    # Imprimer la température de bruit équivalente
    if T_type == '2':
        Teq_db = 10*log10(T)
        print("La température de bruit\n"
              "équivalente Teq est:\n",
              "{:.3e}".format(Teq_db), "dB")
    elif T_type == '1':
        print("La température de bruit\n"
              "équivalente Teq est:\n",
              "{:.3e}".format(T))

################################################################################

def information():
    while True:
        input("Appuyez sur entrer pour\n"
              "continuer")
        print("1. Arbre probabilités")
        print("2. Calculer H(x)")
        print("3. Calculer R")
        print("4. Calculer L")
        print("5. Calculer le rendement n")
        print("6. Calculer le code de Huffman")
        print("7. Sortir")
        
        choice = input("Entrer votre choix: ")
        
        if choice == '1':
            stat()
        elif choice == '2':
            calcul_H()
        elif choice == '3':
            calcul_R()
        elif choice == '4':
            calcul_L()
        elif choice == '5':
            calcul_n()
        elif choice == '6':
            huffman()
        elif choice == '7':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez\n"
                  "entrer un chiffre entre 1-7.")

def stat():
    """
    Crée un arbre de probabilités et calcule les probabilités conditionnelles.
    """
    # Demande à l'utilisateur les probabilités
    P_A0 = get_float("Entrez P(A0): ")
    P_B1_A0 = get_float("Entrez P(B1|A0): ")
    P_B0_A1 = get_float("Entrez P(B0|A1): ")

    # Calcule les probabilités restantes
    P_A1 = 1 - P_A0
    P_B0_A0 = 1 - P_B1_A0
    P_B1_A1 = 1 - P_B0_A1

    # Calcule les probabilités conjointes
    P_A0_B0 = P_A0 * P_B0_A0
    P_A0_B1 = P_A0 * P_B1_A0
    P_A1_B0 = P_A1 * P_B0_A1
    P_A1_B1 = P_A1 * P_B1_A1

    # Calcule les probabilités marginales
    P_B0 = P_A0_B0 + P_A1_B0
    P_B1 = P_A0_B1 + P_A1_B1

    # Applique le théorème de Bayes pour calculer les probabilités
    # conditionnelles inverses
    P_A0_B0 = P_A0_B0 / P_B0 if P_B0 != 0 else 0
    P_A0_B1 = P_A0_B1 / P_B1 if P_B1 != 0 else 0
    P_A1_B0 = P_A1_B0 / P_B0 if P_B0 != 0 else 0
    P_A1_B1 = P_A1_B1 / P_B1 if P_B1 != 0 else 0

    # Calcule la probabilité d'erreur
    Pe = P_A0 * P_B1_A0 + P_A1 * P_B0_A1

    # Print the results
    print('P(A0) = {:.3e}'.format(P_A0))
    print('P(B1|A0) = {:.3e}'.format(P_B1_A0))
    print('P(B0|A1) = {:.3e}'.format(P_B0_A1))
    print('P(A1) = {:.3e}'.format(P_A1))
    input("Appuyez sur entrer pour\n"
          "continuer")
    print('P(B0|A0) = {:.3e}'.format(P_B0_A0))
    print('P(B1|A1) = {:.3e}'.format(P_B1_A1))
    print('P(B0) = {:.3e}'.format(P_B0))
    print('P(B1) = {:.3e}'.format(P_B1))
    input("Appuyez sur entrer pour\n"
          "continuer")
    print('P(A0|B0) = {:.3e}'.format(P_A0_B0))
    print('P(A0|B1) = {:.3e}'.format(P_A0_B1))
    print('P(A1|B0) = {:.3e}'.format(P_A1_B0))
    print('P(A1|B1) = {:.3e}'.format(P_A1_B1))
    print('Pe = {:.3e}'.format(Pe))

def calcul_H():
    """
    Calcule l'entropie H(x) d'une source de données.
    """
    # Demander à l'utilisateur le nombre de symboles
    nombre_symboles = int(input("Entrez le nombre de\n"
                                "symboles: "))
    probabilites = []

    # Demander à l'utilisateur la probabilité de chaque symbole
    for i in range(nombre_symboles):
        p = float(input("Entrez la probabilité du\n"
                        "symbole {} :\n".format(i+1)))
        probabilites.append(p)

    # Calculer l'entropie H(x)
    H_x = sum([-p * log2(p) for p in probabilites])

    # Afficher l'entropie
    print("H(x) =\n{}".format("{:.3e}".format(H_x)))
    return H_x
    
def calcul_R():
    """
    Calcule R = r.H(X) .
    """
    # Demander à l'utilisateur la valeur de r
    r = get_float("Entrez la valeur de r\n"
                  "(symbole/s):\n")

    while True:
        # Demander à l'utilisateur si H(X) est connu
        H_known = input("La valeur de H(X) est-elle\n"
                        "connue ? Oui (1) ou non\n"
                        "(2)? (1/2): ")
        if H_known in ['1', '2']:
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, ou\n"
                  "'2' pour non.")

    if H_known == '1':
        H_x = get_float("Entrez la valeur de H(X):\n")
    else:
        # Si H(X) n'est pas connu, utiliser la fonction calcul_H
        # pour le déterminer
        H_x = calcul_H()

    # Calculer R
    R = r * H_x

    # Afficher R
    print("R =\n{}".format("{:.3e}".format(R)))
    
def calcul_L():
    """
    Calcule L = sum(pj * lj).
    """
    # Demander à l'utilisateur le nombre de symboles
    nombre_symboles = get_positive_int("Entrez le nombre de\n"
                                       "symboles: ")
    L = 0

    # Pour chaque symbole, demander à l'utilisateur la probabilité pj et le
    # nombre de bits lj, puis ajouter pj * lj à L
    for i in range(nombre_symboles):
        p = get_float("Entrez la probabilité du\n"
                      "symbole {}: ".format(i+1))
        l = get_positive_int("Entrez le nombre de bits\n"
                             "pour le symbole {}: ".format(i+1))
        L += p * l

    # Afficher L
    print("L =\n{}".format("{:.3e}".format(L)))
    
    return L
    
def calcul_n():
    """
    Calcule le rendement n = H/L.
    """
    # Demander à l'utilisateur si H et L sont connus
    while True:
        H_known = input("La valeur de H est-elle\n"
                        "connue ?  Oui (1) ou non\n"
                        "(2)? (1/2): ")
        if H_known in ['1', '2']:
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, ou\n"
                  "'2' pour non.")
    while True:
        L_known = input("La valeur de L est-elle\n"
                        "connue ?  Oui (1) ou non\n"
                        "(2)? (1/2): ")
        if L_known in ['1', '2']:
            break
        else:
            print("Réponse invalide. Veuillez\n"
                  "répondre '1' pour oui, ou\n"
                  "'2' pour non.")

    if H_known == '1':
        H = get_float("Entrez la valeur de H:\n")
    else:
        # Si H n'est pas connu, utiliser la fonction calcul_H pour le déterminer
        H = calcul_H()

    if L_known == '1':
        L = get_float("Entrez la valeur de L:\n")
    else:
        # Si L n'est pas connu, utiliser la fonction calcul_L pour le déterminer
        L = calcul_L()

    # Calculer n
    n = H / L

    # Afficher n
    print("n =\n{}".format("{:.3e}".format(n)))

def huffman():
    # Demander le nombre de symboles
    num_symbols = get_positive_int("Entrez le nombre de\n"
                                   "symboles: ")

    # Demander les probabilités
    p = [get_float("Entrez la probabilité du\n"
                   "symbole {}:\n".format(i+1)) for i in range(num_symbols)]

    # Créer une liste avec les feuilles pour chaque symbole
    queue = [{'weight': weight, 'symbol': symbol, 'is_leaf': True} for symbol,
             weight in enumerate(p)]
    queue.sort(key=lambda x: x['weight'])

    # Tant qu'il y a plus d'un nœud dans la file d'attente
    while len(queue) > 1:
        # Retirer les deux nœuds avec les plus petites probabilités
        lo = queue.pop(0)
        hi = queue.pop(0)

        # Créer un nouveau nœud et l'insérer dans la file d'attente
        new_node = {'weight': lo['weight'] + hi['weight'], 'left': lo,
                    'right': hi, 'is_leaf': False}
        queue.append(new_node)
        queue.sort(key=lambda x: x['weight'])

    # Construire le code Huffman à partir de l'arbre
    code = {}
    order = []
    def traverse(node, prefix = ""):
        if node['is_leaf']:
            code[node['symbol']] = prefix
            order.append(node['symbol'])
        else:
            traverse(node['left'], prefix + "0")
            traverse(node['right'], prefix + "1")

    traverse(queue[0])

    # Imprimer les codes Huffman dans l'ordre
    print("Symbole\tPoids\tCode Huffman")
    for symbol in order:
        print("{}\t{}\t{}".format(symbol, p[symbol], code[symbol]))

    # Calculer L, H(X) et n
    L = sum(p[symbol] * len(code[symbol]) for symbol in code)
    H = -sum(p[symbol] * log2(p[symbol]) for symbol in code)
    n = H / L
    
    input("Appuyez sur entrer pour\n"
          "continuer")

    print("L =\n{}".format("{:.3e}".format(L)))
    print("H(X) =\n{}".format("{:.3e}".format(H)))
    print("n =\n{}".format("{:.3e}".format(n)))
    
    input("Appuyez sur entrer pour\n"
          "continuer")

    def plot_tree(node, x=0.5, y=0.5, dx=0.25, dy=0.1):
        if not node['is_leaf']:
            # Draw lines using plot
            plt.plot([x-dx, x+dx], [y, y])  # horizontal line
            plt.plot([x-dx, x-dx], [y, y-dy])  # vertical line to the left child
            plt.plot([x+dx, x+dx], [y, y-dy])  # vertical line to the right child
            plot_tree(node['left'], x-dx, y-dy, dx//2, dy)
            plot_tree(node['right'], x+dx, y-dy, dx//2, dy)
        else:  # Leaf
            plt.plot([x, x], [y, y])  # plot a small line for the leaf

        plt.axis([0, 1, 1, 0])  # set the plot limits and flip the y-axis

    # Draw the Huffman tree
    plot_tree(queue[0])

    plt.show()

################################################################################

def main():
    """
    Fonction principale qui affiche le menu et gère les choix de l'utilisateur.
    """
    while True:
        input("Appuyez sur entrer pour\n"
              "continuer")
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
            print("Choix invalide. Veuillez\n"
                  "entrer un chiffre entre 1-4.")

main()
