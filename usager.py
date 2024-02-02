class Usager:
    def __init__(self, etage, destination):
        self.etage = etage
        self.destination = destination
        self.distrait = False

    def appeler_ascenseur(self, ascenseur):
        ascenseur.ajouter_destination(self.etage)

    def entrer_ascenseur(self, ascenseur):
        if ascenseur.etage_actuel == self.etage and not ascenseur.arret:
            print(f"Usager à l'étage {self.etage} entre dans l'ascenseur.")
            ascenseur.ouvrir_porte()
            ascenseur.ajouter_destination(self.destination)
            ascenseur.fermer_porte()
