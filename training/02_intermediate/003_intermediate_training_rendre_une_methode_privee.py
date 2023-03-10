"""
Rendre une méthode privée
    La classe MachineACafe permet de faire du café et dispose pour ce faire de
    trois méthodes:
        chauffe_eau
        moud_cafe
        fait_du_cafe
    Dans le code de départ, ces trois méthodes sont accessibles directement par
    l'instance.
    Cependant, on aimerait restreindre l'accès aux méthodes chauffe_eau et
    moud_cafe qui n'ont pas vocation à être utilisée directement par
    l'utilisateur mais uniquement par la méthode fait_du_cafe.
    Vous devez donc rendre ces deux méthodes privées et adapter le code de la
    méthode fait_du_cafe pour utiliser ces méthodes privées.

Astuces:
    Bien que cet exercice soit dans la catégorie intermédiaire, si vous savez
    ce qu'est une méthode privée, cet exercice est très simple à réaliser.
    Il ne faut modifier que très peu de choses dans le code initial.
"""


class MachineACafe:
    def __init__(self):
        self.temperature_eau = 0

    def chauffe_eau(self):
        self.temperature_eau = 100
        print("L'eau est chaude.")

    def moud_cafe(self):
        print("Café moulu avec succès.")

    def fait_du_cafe(self):
        self.moud_cafe()
        self.chauffe_eau()
        print("Le café est prêt")


machine = MachineACafe()
machine.fait_du_cafe()
