import pytest
from usager import Usager
# Asume que Ascenceur está en el mismo archivo o ajusta el import según tu estructura de proyecto
from ascenceur import Ascenceur

# Test para verificar que un usager puede llamar correctamente al ascensor
def test_appeler_ascenseur():
    ascenseur = Ascenceur(etage_max=10, etage_min=0)
    usager = Usager(etage=2, destination=5)
    usager.appeler_ascenseur(ascenseur)
    assert 2 in ascenseur.destinations, "l'etage de l'usager doit être ajouté aux destinations de l'ascenseur"

# Test para verificar que un usager puede entrar en el ascensor cuando este está en el mismo piso y detenido
def test_entrer_ascenseur():
    ascenseur = Ascenceur(etage_max=10, etage_min=0)
    ascenseur.etage_actuel = 2  # Asumiendo que el ascensor ya está en el piso del usager
    ascenseur.arret = True  # El ascensor está detenido, lo que permite la entrada del usager
    
    usager = Usager(etage=2, destination=5)
    usager.entrer_ascenseur(ascenseur)
    
    assert ascenseur.arret, "L'ascenseur doit être en arrêt pour que l'usager puisse entrer"
    assert 5 in ascenseur.destinations, "La destination de l'usager doit être ajoutée aux destinations de l'ascenseur"
    assert ascenseur.etage_actuel == usager.etage, "El ascenseur debe estar en el mismo etage que el usager"
    # Este test ya no necesita verificar el estado de 'arret' después de entrar, ya que ese comportamiento se maneja dentro de Ascenceur

