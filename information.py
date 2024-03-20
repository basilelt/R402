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
    H = -sum(p[symbol] * math.log2(p[symbol]) for symbol in code)

    print(f"L = {L}")
    print(f"H(X) = {H}")

    return code

