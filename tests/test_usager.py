
from usager import Usager
from ascenceur import Ascenceur

# Test pour vérifier que l'usager peut appeler l'ascenseur
def test_appeler_ascenseur():
    ascenseur = Ascenceur(etage_max=10, etage_min=0)
    usager = Usager(etage=2, destination=5, distrait=False)
    usager.appeler_ascenseur(ascenseur)
    assert 2 in ascenseur.destinations, "l'etage de l'usager doit être ajouté aux destinations de l'ascenseur"

# Test pour vérifier que l'usager peut entrer dans l'ascenseur
def test_entrer_ascenseur():
    ascenseur = Ascenceur(etage_max=10, etage_min=0)
    ascenseur.etage_actuel = 2  # L'ascenseur est au même étage que l'usager
    ascenseur.arret = True  # L'ascenseur est en arrêt
    
    usager = Usager(etage=2, destination=5, distrait=False)
    usager.entrer_ascenseur(ascenseur)
    
    assert ascenseur.arret, "L'ascenseur doit être en arrêt pour que l'usager puisse entrer"
    assert 5 in ascenseur.destinations, "La destination de l'usager doit être ajoutée aux destinations de l'ascenseur"
    assert ascenseur.etage_actuel == usager.etage, "El ascenseur debe estar en el mismo etage que el usager"

def test_entrer_ascenseur_mauvais_etage():
    ascenseur = Ascenceur(etage_max=10, etage_min=0)
    ascenseur.etage_actuel = 2  # L'ascenseur est au même étage que l'usager
    ascenseur.arret = True  # L'ascenseur est en arrêt
    
    usager = Usager(etage=3, destination=5, distrait=False)
    usager.entrer_ascenseur(ascenseur)
    
    assert ascenseur.arret, "L'ascenseur ne doit pas être en arrêt pour que l'usager puisse entrer"
    assert 5 not in ascenseur.destinations, "La destination de l'usager ne doit pas être ajoutée aux destinations de l'ascenseur"
    assert ascenseur.etage_actuel != usager.etage, "El ascenseur no debe estar en el mismo etage que el usager"

def test_etage():
    usager = Usager(etage=3, destination=5, distrait=False)
    assert usager.etage == 3, "L'attribut etage doit être initialisé correctement"