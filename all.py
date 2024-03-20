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

#####################################################################################################################

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

#####################################################################################################################


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
    while True:
        F_type = input("Le facteur de bruit F est-il en dB (1) ou linéaire (2)? (1/2): ")
        if F_type not in ['1', '2']:
            print("Entrée non valide. Veuillez entrer '1' pour dB ou '2' pour la valeur linéaire.")
        else:
            break
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
    return Feq_db

def calcul_Teq():
    """
    Calcule la température de bruit équivalente Teq.
    """
    n = get_positive_int("Entrez le nombre de quadrupôles n: ")
    while True:
        T_type = input("La température de bruit T est-elle en K (1) ou en dB (2)? (1/2): ")
        if T_type not in ['1', '2']:
            print("Entrée non valide. Veuillez entrer '1' pour K ou '2' pour la valeur en dB.")
        else:
            break

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

#####################################################################################################################

from math import log2

def information():
    while True:
        print("1. Arbre statistic")
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
            print("Choix invalide. Veuillez entrer un chiffre entre 1-3.")

def stat():
    """
    Crée un arbre statistique et calcule les probabilités conditionnelles.
    """
    p_A0 = float(input("Enter the value for P(A0): "))
    p_B1_given_A0 = float(input("Enter the value for P(B1|A0): "))
    p_B0_given_A1 = float(input("Enter the value for P(B0|A1): "))

    p_A1 = 1 - p_A0
    p_B0 = p_A0 * (1 - p_B1_given_A0) + p_A1 * p_B0_given_A1
    p_B1 = 1 - p_B0

    p_A0_given_B0 = (p_A0 * (1 - p_B1_given_A0)) / p_B0
    p_A1_given_B1 = (p_A1 * (1 - p_B0_given_A1)) / p_B1

    p_e = p_A0 * p_B1_given_A0 + p_A1 * p_B0_given_A1

    print(f"P(B0) = { "{:.3e}".format(p_B0)}")
    print(f"P(B1) = { "{:.3e}".format(p_B1)}")
    print(f"P(A0|B0) = { "{:.3e}".format(p_A0_given_B0)}")
    print(f"P(A1|B1) = { "{:.3e}".format(p_A1_given_B1)}")
    print(f"P(e) = { "{:.3e}".format(p_e)}")

    print(f"""
    A0({ "{:.3e}".format(p_A0)})  ----------------- B0({ "{:.3e}".format(p_B0)}) 
                 | B1({ "{:.3e}".format(p_B1_given_A0)})
                 |
    A1({ "{:.3e}".format(p_A1)})  ----------------- B1({ "{:.3e}".format(p_B1)})
                 | B0({ "{:.3e}".format(p_B0_given_A1)})
    """)


def calcul_H():
    """
    Calcule l'entropie H(x) d'une source de données.
    """
    # Demander à l'utilisateur le nombre de symboles
    nombre_symboles = int(input("Entrez le nombre de symboles : "))
    probabilites = []

    # Demander à l'utilisateur la probabilité de chaque symbole
    for i in range(nombre_symboles):
        p = float(input(f"Entrez la probabilité du symbole {i+1} : "))
        probabilites.append(p)

    # Calculer l'entropie H(x)
    H_x = sum([-p * log2(p) for p in probabilites])

    # Afficher l'entropie
    print(f"H(x) = {H_x}")
    
def calcul_R():
    """
    Calcule R = r.H(X) .
    """
    # Demander à l'utilisateur la valeur de r
    r = float(input("Entrez la valeur de r (symbole/s): "))

    while True:
        # Demander à l'utilisateur si H(X) est connu
        H_known = input("La valeur de H(X) est-elle connue ? Oui (1) ou non (2)? (1/2): ")
        if H_known in ['1', '2']:
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, ou '2' pour non.")

    if H_known == '1':
        H_x = float(input("Entrez la valeur de H(X): "))
    else:
        # Si H(X) n'est pas connu, utiliser la fonction calcul_H pour le déterminer
        H_x = calcul_H()

    # Calculer R
    R = r * H_x

    # Afficher R
    print(f"R = {R}")
    
def calcul_L():
    """
    Calcule L = sum(pj * lj).
    """
    # Demander à l'utilisateur le nombre de symboles
    nombre_symboles = int(input("Entrez le nombre de symboles : "))
    L = 0

    # Pour chaque symbole, demander à l'utilisateur la probabilité pj et le nombre de bits lj, puis ajouter pj * lj à L
    for i in range(nombre_symboles):
        p = float(input(f"Entrez la probabilité du symbole {i+1} : "))
        l = int(input(f"Entrez le nombre de bits pour le symbole {i+1} : "))
        L += p * l

    # Afficher L
    print(f"L = {L}")
    
def calcul_n():
    """
    Calcule le rendement n = H/L.
    """
    # Demander à l'utilisateur si H et L sont connus
    while True:
        H_known = input("La valeur de H est-elle connue ?  Oui (1) ou non (2)? (1/2): ")
        if H_known in ['1', '2']:
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, ou '2' pour non.")
    while True:
        L_known = input("La valeur de L est-elle connue ?  Oui (1) ou non (2)? (1/2): ")
        if L_known in ['1', '2']:
            break
        else:
            print("Réponse invalide. Veuillez répondre '1' pour oui, ou '2' pour non.")

    if H_known == '1':
        H = float(input("Entrez la valeur de H : "))
    else:
        # Si H n'est pas connu, utiliser la fonction calcul_H pour le déterminer
        H = calcul_H()

    if L_known == '1':
        L = float(input("Entrez la valeur de L : "))
    else:
        # Si L n'est pas connu, utiliser la fonction calcul_L pour le déterminer
        L = calcul_L()

    # Calculer n
    n = H / L

    # Afficher n
    print(f"n = {n}")

# A node in the Huffman tree
class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# A leaf in the Huffman tree
class Leaf:
    def __init__(self, symbol):
        self.symbol = symbol

def huffman():
    # Demander le nombre de symboles
    num_symbols = int(input("Entrez le nombre de symboles : "))

    # Demander les probabilités
    p = [float(input(f"Entrez la probabilité du symbole {i+1} : ")) for i in range(num_symbols)]

    # Créer une liste avec les feuilles pour chaque symbole
    queue = [(weight, Leaf(symbol)) for symbol, weight in enumerate(p)]
    queue.sort()

    # Tant qu'il y a plus d'un nœud dans la file d'attente
    while len(queue) > 1:
        # Retirer les deux nœuds avec les plus petites probabilités
        lo = queue.pop(0)
        hi = queue.pop(0)

        # Créer un nouveau nœud et l'insérer dans la file d'attente
        new_node = (lo[0] + hi[0], Node(lo[1], hi[1]))
        queue.append(new_node)
        queue.sort()

    # Construire le code Huffman à partir de l'arbre
    code = {}
    def traverse(node, prefix = ""):
        if isinstance(node, Leaf):
            code[node.symbol] = prefix
        else:
            traverse(node.left, prefix + "0")
            traverse(node.right, prefix + "1")

    traverse(queue[0][1])

    # Calculer L et H(X)
    L = sum(p[symbol] * len(code[symbol]) for symbol in code)
    H = -sum(p[symbol] * log2(p[symbol]) for symbol in code)

    print(f"L = {L}")
    print(f"H(X) = {H}")

    return code

#####################################################################################################################

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
