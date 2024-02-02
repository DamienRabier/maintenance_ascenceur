from ascenceur import Ascenceur
from portes import Portes
from usager import Usager

def main():
    # Inicialización de los componentes del sistema
    etage_max = 10
    etage_min = 0
    ascenseur = Ascenceur(etage_max, etage_min)
    portes = {etage: Portes(etage) for etage in range(etage_min, etage_max + 1)}
    usagers = [
        Usager(etage=0, direction="haut", destination=5, distrait=False),
        Usager(etage=3, direction="bas", destination=1, distrait=True)
    ]

    # Simulación de llamadas al ascensor
    for usager in usagers:
        print(usager)
        usager.appeler_ascenceur(ascenseur)

    # Proceso de movimiento del ascensor
    while ascenseur.appels or ascenseur.destinations:
        ascenseur.bouger()
        etage_actuel = ascenseur.getEtage()
        print(f"L'ascenseur arrive à l'étage {etage_actuel}.")

        # Verificar si el ascensor debe detenerse en este piso
        ascenseur.doitArreter()
        if ascenseur.getArret():
            # Simular apertura de puertas
            portes[etage_actuel].ouvrir()
            ascenseur.signalerOuverture(portes[etage_actuel])

            # Embarque de pasajeros
            for usager in usagers:
                if usager.getEtage() == etage_actuel and usager.entrerOuNon():
                    ascenseur.addPassagers(usager)
                    print(f"Usager au {usager.getEtage()} entre dans l'ascenseur.")

            # Cerrar puertas y reanudar movimiento
            portes[etage_actuel].fermer()
            ascenseur.supprimeAppelDestinationEtageCourant()
            ascenseur.setArret(False)

        # Decidir la próxima dirección del ascensor
        ascenseur.renverser()

if __name__ == "__main__":
    main()
