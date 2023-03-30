# Importer le module sys pour accéder aux arguments passés en ligne de commande
# et pour utiliser sys.exit() pour quitter le programme
import sys

# Définition de la fonction rotate_left pour décaler les éléments d'une liste vers la gauche
def rotate_left(elements):
    # On retourne une nouvelle liste composée des éléments de la liste initiale à partir du deuxième (index 1)
    # jusqu'à la fin, puis on ajoute le premier élément (index 0) à la fin de la nouvelle liste
    return elements[1:] + [elements[0]]

# Fonction principale qui prend en paramètre la liste des arguments passés au programme
def main(args):
    # Si le nombre d'arguments est inférieur à 2 (le premier argument est le nom du script lui-même)
    if len(args) < 2:
        # Afficher un message d'erreur et quitter le programme avec un code de sortie non nul (1)
        print("Erreur : veuillez fournir au moins un argument.")
        sys.exit(1)

    # Appeler la fonction rotate_left pour décaler les éléments de la liste args[1:] vers la gauche
    rotated_elements = rotate_left(args[1:])
    # Afficher les éléments décalés, séparés par des virgules
    print(', '.join(rotated_elements))

# Si ce fichier est exécuté en tant que script principal, appeler la fonction main avec les arguments de la ligne de commande
if __name__ == "__main__":
    main(sys.argv)