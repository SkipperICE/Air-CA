# recuperer la liste en argument et s'assurer qu'elle est trier et que c'est bien un int(sans prendre le dernier argument)
#Prendre le dernier argument pour s'assurer que c'est un int
#Boucle for pour le placer dans la liste via une fonction





import sys

def sorted_insert(array, new_element):
    # Vérifier si les arguments sont valides
    if not isinstance(array, list) or not all(isinstance(x, int) for x in array) or not isinstance(new_element, int):
        print("Erreur : Veuillez fournir une liste d'entiers triée et un nouvel entier.")
        sys.exit(1)

    # Boucler à travers la liste pour trouver l'emplacement où insérer le nouvel élément
    for i in range(len(array)):
        if array[i] > new_element:
            array.insert(i, new_element)
            return array

    # Si on a parcouru toute la liste sans insérer le nouvel élément, l'insérer à la fin
    array.append(new_element)
    return array

if __name__ == "__main__":
    # Récupérer la liste triée et le nouvel entier depuis les arguments de la ligne de commande
    args = sys.argv[1:]
if len(args) < 2 or not args[-1].isdigit():
    print("Erreur : Veuillez fournir une liste d'entiers triée et un nouvel entier.")
    sys.exit(1)

if len(args) < 2 or not all(x.isdigit() for x in args[:-1]) or not args[-1].isdigit():
    print("Erreur : Veuillez fournir une liste d'entiers triée et un nouvel entier.")
    sys.exit(1)

array = [int(x) for x in args[:-1]]
new_element = int(args[-1])

# Appeler la fonction sorted_insert pour ajouter le nouvel entier et trier la liste
result = sorted_insert(array, new_element)

# Afficher la liste triée
print(" ".join([str(x) for x in result]))