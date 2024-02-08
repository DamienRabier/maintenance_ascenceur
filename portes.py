from ascenceur import Ascenceur

class Portes:
    def __init__(self, etage):
        self.etage = etage
        self.ouvert = False

    def getEtage(self):
        return self.etage
    def setEtage(self, etage):
        self.etage = etage

    def getOuvert(self):
        return self.ouvert
    def setOuvert(self, ouvert):
        self.ouvert = ouvert

    def __str__(self):
        return "Etage: " + str(self.etage)
    
    def ouvrir(self):
        self.setOuvert(True)
        print(f"Porte ouverte à l'étage {self.etage}...")
    
    def fermer(self):
        self.setOuvert(False)
        print(f"Porte fermée à l'étage {self.etage}...")

