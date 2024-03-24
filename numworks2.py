def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("La valeur doit être un\n"
                      "nombre entier positif.\n"
                      "Veuillez réessayer.")
                continue
            return value
        except ValueError:
            print("Entrée invalide. Veuillez\n"
                  "entrer un nombre entier.")
def hamming():
    while True:
        input("Appuyez sur entrer pour\n"
              "continuer")
        print("1. Calculer le nombre\n"
              "   de bits de parité (m)")
        print("2. Calculer le nombre\n"
              "   de bits de données (k)")
        print("3. Calculer la longueur\n"
              "   du bloc (n)")
        print("4. Calculer la matrice\n"
              "   des codes (C), dmin,\n"
              "   la matrice de parité (H)\n"
              "   et les syndromes (S)")
        print("5. Sortir")
        choice = input("Entrer votre choix: ")
        if choice == '1':
            calcul_m()
        elif choice == '2':
            calcul_k()
        elif choice == '3':
            calcul_n()
        elif choice == '4':
            calcul_C_dmin_H_S()
        elif choice == '5':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez\n"
                  "entrer un chiffre entre 1-5.")
def calcul_m():
    """
    Calcule le nombre de bits de parité m.
    """
    k = get_positive_int("Entrez le nombre de\n"
                         "bits de données k: ")
    n = get_positive_int("Entrez la longueur du\n"
                         "bloc n: ")
    m = n - k
    print("Le nombre de bits de\n"
          "parité m est: ", m)
def calcul_k():
    """
    Calcule le nombre de bits de données k.
    """
    m = get_positive_int("Entrez le nombre de\n"
                         "bits de parité m: ")
    k = 2**m - m - 1
    print("Le nombre de bits de\n"
          "données k est: ", k)
def calcul_n():
    """
    Calcule la longueur du bloc n.
    """
    m = get_positive_int("Entrez le nombre de\n"
                         "bits de parité m: ")
    n = 2**m - 1
    print("La longueur du bloc n est: ", n)
def calcul_C_dmin_H_S():
    """
    Calcule la matrice des codes C.
    """
    def generate_combinations(n):
        if n == 0:
            return [[]]
        else:
            combinations = []
            for combination in generate_combinations(n - 1):
                combinations += [combination + [0], combination + [1]]
            return combinations
    M = []
    cols = get_positive_int("Entrez le nombre de\n"
                            "colonnes de la matrice M: ")
    M = generate_combinations(cols)
    G = []
    rows = get_positive_int("Entrez le nombre de\n"
                            "rangées de la matrice G: ")
    cols = get_positive_int("Entrez le nombre de\n"
                            "colonnes de la matrice G: ")
    for i in range(rows):
        row = []
        for j in range(cols):
            element = get_positive_int("Entrez l'élément de la\n"
                                       "matrice G à la position\n"
                                       "({}, {}):\n".format(i+1, j+1))
            row.append(element)
        G.append(row)
    if len(M[0]) != len(G):
        print("Les dimensions de M et G ne sont pas compatibles.")
        return
    C = []
    for i in range(len(M)):
        row = []
        for j in range(len(G[0])):
            element = 0
            for k in range(len(G)):
                element += M[i][k] * G[k][j]
            element = element % 2
            row.append(element)
        C.append(row)
    print("La matrice des codes C est:")
    for row in C:
        print(row)
        input()
    input("Appuyez sur entrer pour\n"
          "continuer")
    dmin = min(sum(a != b for a, b in zip(C[i], C[j]))
               for i in range(len(C)) for j in range(i+1, len(C)))
    print("La distance minimale dmin est:\n", dmin)
    print("La capacité de détecter\n"
          "les erreurs est:\n", dmin - 1)
    print("La capacité de correction\n"
          "d'erreur est:\n", (dmin - 1) // 2)
    input("Appuyez sur entrer pour\n"
          "continuer")
    n, k = len(G[0]), len(G)
    P_transpose = list(map(list, zip(*G)))[:k]
    I = [[int(i == j) for j in range(n - k)] for i in range(n - k)]
    H = [I[i] + P_transpose[i] for i in range(n - k)]
    print("La matrice de parité H est:")
    for row in H:
        print(row)
    H_transpose = list(map(list, zip(*H)))
    while True:
        print("0. Arrêter de calculer les syndromes")
        print("1. Calculer un syndrome")
        print("2. Calculer tous les syndromes")
        choice = input("Entrer votre choix: ")
        if choice == '0':
            break
        elif choice == '1':
            c = []
            rows = 1
            cols = get_positive_int("Entrez le nombre de\n"
                                    "colonnes de la matrice c: ")
            for i in range(rows):
                row = []
                for j in range(cols):
                    element = get_positive_int("Entrez l'élément de la\n"
                                               "matrice c à la position\n"
                                               "({}, {}):\n".format(i+1, j+1))
                    row.append(element)
                c.append(row)
            S = []
            for i in range(len(c)):
                row = []
                for j in range(len(H_transpose[0])):
                    element = 0
                    for k in range(len(c[0])):
                        element += c[i][k] * H_transpose[k][j]
                    element = element % 2
                    row.append(element)
                S.append(row)
            print("Le syndrome est:")
            for row in S:
                print(row)
                input()
        elif choice == '2':
            S = []
            for i in range(len(C)):
                row = []
                for j in range(len(H_transpose[0])):
                    element = 0
                    for k in range(len(C[0])):
                        element += C[i][k] * H_transpose[k][j]
                    element = element % 2
                    row.append(element)
                S.append(row)
            print("Les syndromes sont:")
            for row in S:
                print(row)
                input()
def convolutif():
    e = []
    e_n = input("Entrez le nombres d'entrées e:\n")
    for i in range(e):
        e.append(get_positive_int("Entrez l'état initial s{}:\n".format(i+1)))
    et_in = []
    reg = []
    et_fin = []
    et_in.append([0,0])
    sort = []
    print("Entrée    Etat initial    Registre    Etat final    Sortie")
    for i in range(e_n):
        reg.append([e[i], et_in[i][0], et_in[i][1]])
        et_fin.append([e[i], et_in[i][0]])
        sort.append([(e[i]^et_in[i][0])^et_in[i][1], e[i]^et_in[i][0]])
        print("{}    {}              {}          {}            {}".format(e[i],
              et_in[i], reg[i], et_fin[i], sort[i]))
        et_in.append([e[i], et_in[i][1]])
def main():
    while True:
        input("Appuyez sur entrer pour\n"
              "continuer")
        print("1. Hamming (n,k)")
        print("2. Convolutif")
        print("3. Sortir")
        choice = input("Entrer votre choix: ")
        if choice == '1':
            hamming()
        elif choice == '2':
            convolutif()
        elif choice == '3':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez\n"
                  "entrer un chiffre entre 1-3.")
main()