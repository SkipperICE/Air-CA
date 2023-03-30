import sys

def ma_fonction(array_de_strings, separateur):
    string = separateur.join(array_de_strings)
    return string

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Erreur : veuillez fournir au moins deux arguments : un tableau de chaînes de caractères à fusionner et un séparateur.")
        sys.exit(1)
    else:
        array_de_strings = sys.argv[1:-1]
        separateur = sys.argv[-1]
        string = ma_fonction(array_de_strings, separateur)
        print(string)