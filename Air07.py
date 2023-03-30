import sys

def ma_fonction(array_de_strings, string):
    # Vérifier si les arguments sont valides
    if not array_de_strings or not string:
        print("Error: Invalid arguments.Not a String")
        sys.exit()

    # Créer une liste pour stocker les résultats
    result = []

    # Parcourir tous les éléments de la liste
    for s in array_de_strings:
        # Vérifier si la chaîne de caractères est contenue dans l'élément actuel
        if string in s:
            # Ajouter l'élément actuel à la liste de résultats
            result.append(s)

    # Retourner la liste de résultats
    return result

if __name__ == "__main__":
    # Récupérer les arguments depuis la ligne de commande
    args = sys.argv[1:]

if len(sys.argv) <= 2:
        print("Erreur : veuillez fournir au moins un argument : une liste d'éléments à analyser.")
        sys.exit(1)

# Récupérer la liste d'éléments et la chaîne de caractères depuis les arguments
array_de_strings = args[:-1]
string = args[-1]

result = ma_fonction(array_de_strings, string)

# Afficher les résultats
print(", ".join(result))