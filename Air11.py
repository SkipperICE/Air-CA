# Importer le module sys pour accéder aux arguments passés en ligne de commande
# et pour utiliser sys.exit() pour quitter le programme
import sys

def main(args):
    # Vérifier si le nombre d'arguments est différent de 2 (le premier argument est le nom du script lui-même)
    if len(args) != 2:
        # Afficher un message d'erreur et quitter le programme avec un code de sortie non nul (1)
        print("Erreur : veuillez fournir le nom du fichier en argument.")
        sys.exit(1)

    # Stocker le nom du fichier passé en argument
    filename = args[1]

    # Essayer d'ouvrir le fichier en mode lecture ('r')
    try:
        with open(filename, 'r') as file:
            # Lire le contenu du fichier
            content = file.read()
            # Afficher le contenu du fichier
            print(content)
    # Si le fichier n'est pas trouvé, lever une exception FileNotFoundError
    except FileNotFoundError:
        # Afficher un message d'erreur et quitter le programme avec un code de sortie non nul (1)
        print(f"Erreur : le fichier '{filename}' n'a pas été trouvé.")
        sys.exit(1)
    # Si un problème survient lors de la lecture du fichier, lever une exception IOError
    except IOError:
        # Afficher un message d'erreur et quitter le programme avec un code de sortie non nul (1)
        print(f"Erreur : impossible de lire le fichier '{filename}'.")
        sys.exit(1)

# Si ce fichier est exécuté en tant que script principal, appeler la fonction main avec les arguments de la ligne de commande
if __name__ == "__main__":
    main(sys.argv)