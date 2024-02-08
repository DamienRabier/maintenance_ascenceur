from ascenceur import Ascenceur
from usager import Usager

def main():
    ascenseur = Ascenceur(etage_max=10, etage_min=0)
    usagers = [
        Usager(etage=0, destination=5, distrait=False),
        Usager(etage=3, destination=1, distrait=True)
    ]

    for usager in usagers:
        usager.appeler_ascenseur(ascenseur)

    while ascenseur.destinations:
        ascenseur.bouger()
        if ascenseur.etage_actuel in ascenseur.destinations:
            ascenseur.ouvrir_porte()
            for usager in usagers:
                if usager.etage == ascenseur.etage_actuel:
                    usager.entrer_ascenseur(ascenseur)
            ascenseur.fermer_porte()

if __name__ == "__main__":
    main()

