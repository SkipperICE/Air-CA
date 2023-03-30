import sys

def ma_fonction(string_a_couper, string_separateur=None):
    try:
        tableau = string_a_couper.split()
        return tableau
    except AttributeError:
        print("Erreur : veuillez fournir une chaîne de caractères en tant que premier argument.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Erreur : veuillez fournir 1 arguments : une chaîne de caractères")
        sys.exit(1)
    else:
        string_a_couper = sys.argv[1]
        string_separateur = None
        tableau = ma_fonction(string_a_couper, string_separateur)
        print("\n".join(tableau))