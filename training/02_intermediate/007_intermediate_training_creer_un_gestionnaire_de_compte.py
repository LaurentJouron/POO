"""
Créer un gestionnaire de compte
    Cet exercice n'est pas extrêmement compliqué si ce n'est que vous partez
    cette fois-ci de 0 !
    Dans cet exercice vous devez créer une classe Compte qui permette de
    déposer et retirer de l'argent de votre compte bancaire.
    Les instances créées grâce à la classe Compte doivent posséder trois
    attributs :
    nom
    numero
    balance
    Cela permet ainsi de créer un compte pour John, avec un numéro de compte
    de 12345 et un dépot initial de 20,000€ :
    compte_john = Compte(nom="John", numero="12345", balance=20000)
    Nous déposons ensuite 3,000€ supplémentaires grâce à la méthode deposer.
    Pour finir, nous retirons 200€ grâce à la méthode retirer.
    Vous devez donc créer la classe Compte et toutes les méthodes nécessaires
    pour que le code fonctionne.
    L'attribut balance du compte de John doit contenir à la fin du script
    22,800€ (20,000 + 3,000 - 200).
"""


compte_john = Compte(nom="John", numero="12345", balance=20000)
compte_john.deposer(montant=3000)
compte_john.retirer(montant=200)