import random
import string

def generer_mot_de_passe(longueur=12, utiliser_chiffres=True, utiliser_symboles=True):
    caracteres = string.ascii_letters  # 
    if utiliser_chiffres:
        caracteres += string.digits  #
    if utiliser_symboles:
        caracteres += string.punctuation  # 

    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

print(generer_mot_de_passe())
