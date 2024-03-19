from functions import get_float
def information():
    while True:
        print("1. Arbre statistic")
        print("2. ")
        print("3. Sortir")
        
        choice = input("Entrer votre choix: ")
        
        if choice == '1':
            stat()
        elif choice == '2':
            break
        elif choice == '3':
            print("Sortir...")
            break
        else:
            print("Choix invalide. Veuillez entrer un chiffre entre 1-3.")

def stat():
    # Initialize all probabilities to None
    A0 = A1 = B0_given_A0 = B1_given_A1 = B1_given_A0 = B0_given_A1 = A0_given_B1 = A1_given_B0 = None

    # Flag to indicate if the user is finished entering probabilities
    finished = False

    # Get the known probabilities from the user
    A0 = get_float("Enter the probability of transmission of 0 (A0), -1 to skip, or -2 if finished: ")
    if A0 == -1:
        A0 = None
    elif A0 == -2:
        finished = True
    if not finished:
        A1 = get_float("Enter the probability of transmission of 1 (A1), -1 to skip, or -2 if finished: ")
        if A1 == -1:
            A1 = None
        elif A1 == -2:
            finished = True
    if not finished:
        B0_given_A0 = get_float("Enter the probability of reception of 0 given transmission of 0 (P(B0|A0)), -1 to skip, or -2 if finished: ")
        if B0_given_A0 == -1:
            B0_given_A0 = None
        elif B0_given_A0 == -2:
            finished = True
    # ... repeat for the other probabilities ...

    # Calculate the remaining probabilities
    if A0 is None:
        A0 = 1 - A1
    if A1 is None:
        A1 = 1 - A0
    if B0_given_A0 is None:
        B0_given_A0 = 1 - B1_given_A1
    if B1_given_A1 is None:
        B1_given_A1 = 1 - B0_given_A0
    if B1_given_A0 is None:
        B1_given_A0 = 1 - B0_given_A0
    if B0_given_A1 is None:
        B0_given_A1 = 1 - B1_given_A1

    # Calculate the reversed probabilities
    A0_given_B1 = B1_given_A0 * A0 / (B1_given_A0 * A0 + B1_given_A1 * A1)
    A1_given_B0 = B0_given_A1 * A1 / (B0_given_A1 * A1 + B0_given_A0 * A0)

    # Print the statistic tree
    print("Statistique Tree:")
    print("A0: ", A0)
    print("|__ P(B0|A0): ", B0_given_A0)
    print("|__ P(B1|A0): ", B1_given_A0)
    print("A1: ", A1)
    print("|__ P(B0|A1): ", B0_given_A1)
    print("|__ P(B1|A1): ", B1_given_A1)
    print("B0: ")
    print("|__ P(A1|B0): ", A1_given_B0)
    print("B1: ")
    print("|__ P(A0|B1): ", A0_given_B1)