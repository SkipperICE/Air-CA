# Importer le module sys pour accéder aux arguments passés en ligne de commande
# et pour utiliser sys.exit() pour quitter le programme
import sys

def print_staircase(character, num_steps):
    # Parcourir la plage de 1 à num_steps+1 pour créer chaque étage de l'escalier
    for i in range(1, num_steps + 1):
        # Calculer le nombre d'espaces à gauche du caractère pour chaque étage
        spaces = num_steps - i
        # Créer une chaîne de caractères pour chaque étage en répétant le caractère (2*i - 1) fois
        step = character * (2 * i - 1)
        # Afficher l'étage en ajoutant les espaces à gauche du caractère
        print(' ' * spaces + step)

def main(args):
    # Vérifier si le nombre d'arguments est différent de 3 (le premier argument est le nom du script lui-même)
    if len(args) != 3:
        print("Erreur : veuillez fournir un caractère et un nombre d'étages en arguments.")
        sys.exit(1)

    # Stocker le caractère et le nombre d'étages passés en arguments
    character = args[1]
    try:
        num_steps = int(args[2])
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide d'étages.")
        sys.exit(1)

    # Appeler la fonction print_staircase pour afficher l'escalier
    print_staircase(character, num_steps)

# Si ce fichier est exécuté en tant que script principal, appeler la fonction main avec les arguments de la ligne de commande
if __name__ == "__main__":
    main(sys.argv)