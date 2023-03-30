import sys

def quicksort(arr):
    """
    Trie une liste de nombres en utilisant l'algorithme de tri rapide.

    :param arr: la liste de nombres à trier
    :return: la liste triée
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return quicksort(left) + [pivot] + quicksort(right)


if __name__ == "__main__":
    # Vérifie si les arguments sont des nombres, sinon affiche un message d'erreur et quitte le programme
    try:
        nums = [int(num) for num in sys.argv[1:]]
    except ValueError:
        print("Erreur : les arguments doivent être des nombres entiers.")
        sys.exit(1)

    # Trie la liste de nombres
    sorted_nums = quicksort(nums)

    # Affiche la liste triée
    print(" ".join([str(num) for num in sorted_nums]))