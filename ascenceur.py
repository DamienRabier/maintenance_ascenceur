from portes import Portes
from usager import Usager

class Ascenceur:
    def __init__(self, etageActuel, etageMax, etageMin, destinations, appels):
        self.etage = etageActuel
        self.etageMax = etageMax
        self.etageMin = etageMin
        self.direction = "haut"
        self.destinations = destinations
        self.appels = appels
        self.arret = False

    def getEtage(self):
        return self.etage
    def setEtage(self, etage):
        self.etage = etage

    def getEtageMax(self):
        return self.etageMax
    def setEtageMax(self, etageMax):
        self.etageMax = etageMax

    def getEtageMin(self):
        return self.etageMin
    def setEtageMin(self, etageMin):
        self.etageMin = etageMin

    def getDirection(self):
        return self.direction
    def setDirection(self, direction):
        self.direction = direction
    
    def getDestinations(self):
        return self.destinations
    def setDestinations(self, destinations):
        self.destinations = destinations

    def getAppels(self):
        return self.appels
    def setAppels(self, appels):
        self.appels = appels
    
    def getArret(self):
        return self.arret
    def setArret(self, arret):
        self.arret = arret
    
    def __str__(self) -> str:
        return f"Etage: {self.etage}, Direction: {self.direction}, Destinations: {self.destinations}, Appels: {self.appels}"
    
    def monter(self):
        self.etage += 1
    
    def descendre(self):
        self.etage -= 1
    
    def bouger(self):
        if self.direction == "monte" and self.etage < self.etageMax:
            self.monter()
        elif self.direction == "descend" and self.etage > self.etageMin:
            self.descendre()
    
    def renverser(self):
        if self.direction == "monte" and self.etage == self.etageMax:
            self.direction = "descend"
        elif self.direction == "descend" and self.etage == self.etageMin:
            self.direction = "monte"

    def doitArreter(self):
        if self.etage in self.destinations:
            self.setArret(True)
        elif self.etage in self.appels:
            self.setArret(True)
        else:
            self.setArret(False)

    def supprimeAppelDestinationEtageCourant(self):
        if self.etage in self.destinations:
            self.destinations.remove(self.etage)
        if self.etage in self.appels:
            self.appels.remove(self.etage)

    def signalerOuverture(portes):
        portes.setOuvert(True)
        print("Portes ouvertes")