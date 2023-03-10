"""
Gérer les notes d'élèves
    Dans cet exercice, vous partez là encore de zéro.
    Premièrement, vous devez créer une classe Note qui contient un seul
    attribut, valeur, qui correspond à la valeur de la note.
    Vous devez modifier la représentation des instances de cette classe pour
    qu'elles affichent la valeur de la note sur 20, comme ceci :
    #>>> note = Note(valeur=12)
    #>>> note
    '12 / 20'
    Vous devez ensuite créer une classe Notes qui hérite de la classe list et
    qui permet de récupérer une liste d'instances de notes.
    On doit pouvoir ajouter une note à cette classe avec la méthode
    ajouter_note.
    On créera ensuite deux méthodes.
    La première, notes_parfaites, qui retournera le nombre de notes égales à
    20/20.
    La deuxième, moyenne, qui retournera la moyenne des notes.
    Dans le cas de ce script, avec la liste de notes
    [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17],
    ces deux méthodes devront retourner respectivement 2
    (car il y a deux 20/20 dans la liste) et
    14.2 (qui est la moyenne de toutes ces notes).
    La moyenne doit retourner un nombre décimal et être arrondie à une seule
    décimale.

Astuces:
    Pour arrondir un nombre, on peut utiliser la fonction round et passer en
    deuxième argument le nombre de décimales après la virgule que l'on souhaite
    garder.
"""


valeur_notes = [12, 19, 14, 13, 9, 20, 8, 15, 4, 20, 19, 17]
notes = Notes()

for valeur_note in valeur_notes:
    notes.ajouter_note(note=Note(valeur=valeur_note))

print(notes.notes_parfaites())
print(notes.moyenne())