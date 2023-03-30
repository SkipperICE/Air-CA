import sys

def ma_fonction(liste):
    # Récupérer l'opération à appliquer (le dernier élément de la liste)
    operation = liste.pop()
    
    # Vérifier que l'opération commence par "+" ou "-"
    if not (operation.startswith("+") or operation.startswith("-")):
        print("Erreur : opération invalide : {}".format(operation))
        sys.exit(1)
    
    # Extraire l'opérande de l'opération
    try:
        operande = int(operation[1:])
    except ValueError:
        print("Erreur : opération invalide : {}".format(operation))
        sys.exit(1)
    
    # Parcourir la liste et appliquer l'opération à chaque élément
    nouvelle_liste = []
    for element in liste:
        # Vérifier que chaque élément est un nombre
        try:
            valeur = int(element)
        except ValueError:
            print("Erreur : élément de la liste invalide : {}".format(element))
            sys.exit(1)
        
        # Appliquer l'opération à l'élément courant
        if operation.startswith("+"):
            resultat = valeur + operande
        elif operation.startswith("-"):
            resultat = valeur - operande
        
        # Ajouter le résultat à la nouvelle liste
        nouvelle_liste.append(str(resultat))
    
    # Joindre les éléments de la nouvelle liste en une chaîne de caractères
    return " ".join(nouvelle_liste)

if __name__ == "__main__":
    # Vérifier que l'utilisateur a fourni suffisamment d'arguments en ligne de commande
    if len(sys.argv) < 3:
        print("Erreur : veuillez fournir au moins deux arguments : une liste d'entiers et une opération.")
        sys.exit(1)
    else:
        # Récupérer la liste d'entiers à traiter (tous les arguments sauf le dernier)
        liste = sys.argv[1:-1]
        
        # Vérifier que tous les éléments de la liste sont des nombres
        for element in liste:
            try:
                int(element)
            except ValueError:
                print("Erreur : élément de la liste invalide : {}".format(element))
                sys.exit(1)
        
        # Appeler la fonction ma_fonction avec la liste d'entiers et l'opération à appliquer
        resultat = ma_fonction(liste + [sys.argv[-1]])
        print(resultat)