import sys

def ma_fonction(chaine):
    nouvelle_chaine = ""
    precedent = ""
    for caractere in chaine:
        if caractere != precedent:
            nouvelle_chaine += caractere
            precedent = caractere
    return nouvelle_chaine

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Erreur : veuillez fournir un argument : une chaîne de caractères à traiter.")
        sys.exit(1)
    else:
        chaine = sys.argv[1]
        resultat = ma_fonction(chaine)
        print(resultat)