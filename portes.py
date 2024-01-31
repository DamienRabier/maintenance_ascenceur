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
    
    def fermer(self):
        self.setOuvert(False)

    def redemarrer(a : Ascenceur):
        a.setArret(False)
        print("Redémarrage de l'ascenceur...")