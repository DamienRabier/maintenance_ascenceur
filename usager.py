# usager.py
class Usager:
    def __init__(self, etage, destination):
        self.etage = etage
        self.destination = destination
        self.distrait = False  # No se usa en el código actual, pero se deja para futuras expansiones

    def appeler_ascenseur(self, ascenseur):
        ascenseur.ajouter_destination(self.etage)

    def entrer_ascenseur(self, ascenseur):
        # Ajuste: Verificar que el ascensor está en el mismo piso y detenido antes de entrar
        if ascenseur.etage_actuel == self.etage and ascenseur.arret:
            print(f"Usager à l'étage {self.etage} entre dans l'ascenseur.")
            ascenseur.ajouter_destination(self.destination)
            # No necesitas abrir y cerrar la puerta aquí; eso se maneja por el ascensor
