class Usager:
    def __init__(self, etage, direction, destination) -> None:
        #étage courant (int)
        self.etage = etage
        #direction
        self.direction = direction
        #destination (int)
        self.destination = destination

    def __str__(self) -> str:
        return f"Etage: {self.etage}, Direction: {self.direction}, Destination: {self.destination}"
    
    def __eq__(self, o: object) -> bool:
        return self.etage == o.etage and self.direction == o.direction and self.destination == o.destination
    
    def getEtage(self):
        return self.etage
    def setEtage(self, etage):
        self.etage = etage

    def getDirection(self):
        return self.direction
    def setDirection(self, direction):
        self.direction = direction

    def getDestination(self):
        return self.destination
    def setDestination(self, destination):
        self.destination = destination

    def memeDestination(self, usager):
        return self.destination == usager.getDestination()
