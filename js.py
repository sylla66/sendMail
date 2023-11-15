

# Fonction pour obtenir la flèche en fonction de la valeur
def obtenir_fleche_et_couleur(nombre):
    if nombre >= 0:
        classe = 'positif'
        fleche = '&#9650;'  # Flèche vers le haut
    elif nombre < 0:
        classe = 'negatif'
        fleche = '&#9660;'  # Flèche vers le bas
    return f'<span class="{classe}">{fleche}</span>'

# Fonction pour obtenir la classe de couleur en fonction de la valeur
def obtenir_classe_couleur(nombre):
    if nombre >= 0:
        return 'positif'
    elif nombre < 0:
        return 'negatif'
