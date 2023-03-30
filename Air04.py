import sys

def ma_fonction(liste):
    # Créer un dictionnaire pour stocker le nombre d'occurrences de chaque élément de la liste
    compteur = {}
    for element in liste:
        if element not in compteur:
            compteur[element] = 0
        compteur[element] += 1
    
    # Parcourir le dictionnaire et ajouter tous les éléments ayant un nombre d'occurrences impaire à une liste
    elements_impairs = []
    for element, count in compteur.items():
        if count % 2 == 1:
            elements_impairs.append(element)
    
    # Si la liste contient plusieurs éléments, retourner la liste. Sinon, retourner le premier élément de la liste (ou None)
    if len(elements_impairs) == 0:
        return None
    elif len(elements_impairs) == 1:
        return elements_impairs[0]
    else:
        return elements_impairs

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erreur : veuillez fournir au moins un argument : une liste d'éléments à analyser.")
        sys.exit(1)
    else:
        liste = sys.argv[1:]
        resultat = ma_fonction(liste)
        if resultat is None:
            print("Aucun élément de la liste n'a un nombre d'occurrences impaire.")
        elif isinstance(resultat, list):
            print("Plusieurs éléments de la liste ont un nombre d'occurrences impaire :")
            print(", ".join(resultat))
        else:
            print(resultat)