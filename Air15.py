import sys

# Vérifier le nombre d'arguments en ligne de commande
if len(sys.argv) != 2:
    print("Usage: python exo.py <adjectif>")
    sys.exit()

# Récupérer l'adjectif
adjectif = sys.argv[1]

# Afficher le message de victoire
message = f"J'ai terminé l'Épreuve de l'Air et c'était {adjectif} !"
print(message)