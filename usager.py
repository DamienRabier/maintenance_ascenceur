# usager.py
class Usager:
    def __init__(self, etage, destination, distrait):
        self.etage = etage
        self.destination = destination
        self.distrait = distrait  

    def appeler_ascenseur(self, ascenseur):
        ascenseur.ajouter_destination(self.etage)

    def entrer_ascenseur(self, ascenseur):
        # Verifier si l'ascenseur est à l'étage de l'usager et si l'ascenseur est en arrêt
        if ascenseur.etage_actuel == self.etage and ascenseur.arret:
            if not self.distrait:
                print(f"Usager à l'étage {self.etage} entre dans l'ascenseur.")
                ascenseur.ajouter_destination(self.destination)
            else:
                print("Usager distrait ne rentre pas dans l'ascenseur.")
        else:
            print(f"L'ascenseur n'est pas à l'étage {self.etage} ou il n'est pas en arrêt.")
