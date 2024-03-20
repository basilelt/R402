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
