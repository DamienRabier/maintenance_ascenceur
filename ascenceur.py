import unittest

class Ascenceur:
    def __init__(self, etage_max, etage_min):
        self.etage_actuel = 0
        self.etage_max = etage_max
        self.etage_min = etage_min
        self.direction = None  # Puede ser 'haut', 'bas' o None
        self.destinations = []
        self.arret = False

    def ajouter_destination(self, etage):
        if etage not in self.destinations:
            self.destinations.append(etage)
            self.destinations.sort()

    def monter(self):
        if self.etage_actuel < self.etage_max:
            self.etage_actuel += 1
            self.direction = "haut"

    def descendre(self):
        if self.etage_actuel > self.etage_min:
            self.etage_actuel -= 1
            self.direction = "bas"

    def choisir_direction(self):
        if self.destinations:
            if self.etage_actuel < self.destinations[0]:
                self.direction = "haut"
            elif self.etage_actuel > self.destinations[0]:
                self.direction = "bas"
            else:
                self.direction = None
        else:
            self.direction = None

    def bouger(self):
        self.choisir_direction()
        if self.direction == "haut":
            self.monter()
        elif self.direction == "bas":
            self.descendre()

    def ouvrir_porte(self):
        print(f"Porte ouverte à l'étage {self.etage_actuel}.")
        self.arret = True

    def fermer_porte(self):
        print(f"Porte fermée à l'étage {self.etage_actuel}.")
        self.arret = False
        if self.etage_actuel in self.destinations:
            self.destinations.remove(self.etage_actuel)
        
    def redemarrer(self):
        if not self.arret and self.etage_actuel in self.destinations:
            print("Redémarrage de l'ascenseur...")
            self.bouger()
        else:
            print("L'ascenseur est déjà en mouvement ou il n'y a pas de destinations actuelles.")

if __name__ == "__main__":
    unittest.main()
