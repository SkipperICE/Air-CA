import os
import subprocess

# Récupération de la liste des fichiers dans le répertoire courant
files = [f for f in os.listdir('.') if os.path.isfile(f)]

# Parcours des fichiers et vérification de leur exécution
for file in files:
    # On ne teste que les fichiers qui ont une extension .py (en excluant le fichier en cours d'exécution)
    if file.endswith('.py') and file != 'Air14.py':
        # Exécution du programme en utilisant subprocess.run()
        result = subprocess.run(['python3.11', file], capture_output=True, text=True)
        
        # Si le retour est 0, le programme s'est exécuté avec succès
        if result.returncode == 0:
            # Affichage du nom du fichier avec le texte "success" en vert
            print('\033[32m' + file + ': success' + '\033[0m')
        else:
            # Si le retour est différent de 0, le programme a échoué
            # Affichage du nom du fichier avec le texte "failure" en rouge
            print('\033[31m' + file + ': failure' + '\033[0m')