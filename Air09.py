import sys

def merge_sorted_lists(list1, list2):
    # Vérifier si les arguments sont valides
    if not all(isinstance(x, int) for x in list1) or not all(isinstance(x, int) for x in list2):
        print("Erreur : Veuillez fournir deux listes d'entiers triées.")
        sys.exit(1)

    # Vérifier si les listes sont triées
    if list1 != sorted(list1) or list2 != sorted(list2):
        print("Erreur : Les listes doivent être triées.")
        sys.exit(1)

    # Initialiser les indices des deux listes et la liste de fusion
    i = 0
    j = 0
    merged_list = []

    # Boucler jusqu'à ce que l'une des listes soit entièrement traitée
    while i < len(list1) and j < len(list2):
        # Ajouter l'élément le plus petit des deux listes à la liste de fusion
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Ajouter les éléments restants de la première liste à la liste de fusion
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    # Ajouter les éléments restants de la deuxième liste à la liste de fusion
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    # Retourner la liste de fusion
    return merged_list

if __name__ == "__main__":
    # Récupérer les deux listes triées depuis les arguments de la ligne de commande
    args = sys.argv[1:]
    if len(args) < 3 or "fusion" not in args:
        print("Erreur : Veuillez fournir deux listes d'entiers triées séparées par le mot-clé 'fusion'.")
        sys.exit(1)

    idx = args.index("fusion")
    list1 = [int(x) for x in args[:idx]]
    list2 = [int(x) for x in args[idx+1:]]

    # Fusionner les deux listes triées
    merged_list = merge_sorted_lists(list1, list2)

    # Afficher la liste de fusion triée
    print(" ".join([str(x) for x in merged_list]))