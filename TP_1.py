
"""
Renvoyer l’âge à partir d’une année de naissance
En année 
En Nb de mois 
En nb de jours (piège bissextile) 
En nb de semaine
Compter le nombre de mot d’une chaine de caractère saisie
Compter le nombre de voyelle d’une chaine de caractère saisie
Compter le nombre de présence d’une lettre dans d’une chaine de caractère saisie
Renvoyer une liste de mot à partir d’une phrase
Vérifier la présence d’une lettre dans d’une chaine de caractère saisie
Vérifier la présence d’un mot dans une liste (retourne sa position dans le tableau)
Créer une fonction de gestion de liste 
ajoute un mot si il n’est pas présent dans un tableau
Le supprime si il est déjà présent
Renvoie le tableau si on écrit « tableau »
Arrête le programme si on écrit « stop »
"""

# ctrl + a => select all
#  

import datetime

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
anneeActuel = date.strftime("%Y")



anneeNaissance = input("Ajouter votre année de naissance: ")
#anneeActuel = 2000

age = int(anneeActuel) - int(anneeNaissance)
print("Vous avez", age, "ans")
print("Vous avez " + str(age * 12) + " mois")
print("Vous avez " + str(age * 365) + " jour")
print("Vous avez " + str(age * 52) + " semaine")
print("Vous avez " + str(age * 365 + (age/4)) + " jours")

if age <= 17:
    print("Vous n'etes pas majeur")
elif age >= 18:
    print("Vous etes adulte")
else: print("Je Ne Sais Pas quel age vous avez")


annee = int(input("Entrer l'année"))
if annee % 100 == 0:
    if annee % 400 == 0:
        print("{} C'est une année bissextile".format(annee))
    else:
        print("Ce n'est pas une année bissextile".format(annee))
else:
    if annee % 4 == 0:
        print("{} C'est une année bissextile".format(annee))
    else:
        print("{} Ce n'est pas une année bissextile".format(annee))