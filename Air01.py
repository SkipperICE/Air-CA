import sys

def ma_fonction(string_a_couper, string_separateur):
    try:
        tableau = string_a_couper.split(string_separateur)
        return tableau
    except AttributeError:
        print("Erreur : veuillez fournir une chaîne de caractères en tant que premier argument.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Erreur : veuillez fournir deux arguments : une chaîne de caractères à couper et un séparateur.")
        sys.exit(1)
    else:
        string_a_couper = sys.argv[1]
        string_separateur = sys.argv[2]
        tableau = ma_fonction(string_a_couper, string_separateur)
        print("\n".join(tableau))