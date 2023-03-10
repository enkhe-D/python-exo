# Compter le nombre de voyelle d’une chaine de caractère saisie
# Compter le nombre de présence d’une lettre dans d’une chaine de caractère saisie
# Renvoyer une liste de mot à partir d’une phrase
# Vérifier la présence d’une lettre dans d’une chaine de caractère saisie
# Vérifier la présence d’un mot dans une liste (retourne sa position dans le tableau)

maChaine = len
maChaine = "une liste de mots"
print("ma chaine de charactere: " ,maChaine.split(' '))

nbrCharactere = "Hello! on est la promo Grace"
print(len(nbrCharactere))

#######################################################################""

voyelle = {"a", "e", "y", "u", "i","o"}

s = "ma chaine de charactere les decodeuses"
print(s.split(' '))

n = len(s)

nbrVoyelle = 1

for i in range(1, n):
    if(s[i] in voyelle):
        nbrVoyelle += 1
print("Le nombre des voyelle: ", nbrVoyelle)

###########################################################################"

lstMots = ["des", "mots", "toujours", "des", "mots"]
print(lstMots)

###########################################################################