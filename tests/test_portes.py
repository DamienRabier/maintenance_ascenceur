from portes import Portes
from ascenceur import Ascenceur

def test_porte_initial_state():
    portes = Portes(etage=0)
    assert portes.getEtage() == 0
    assert not portes.getOuvert()

def test_porte_ouvrir():
    portes = Portes(etage=1)
    portes.ouvrir()
    assert portes.getOuvert()

def test_porte_fermer():
    portes = Portes(etage=2)
    portes.ouvrir()  # Asegurar que la puerta está abierta antes de intentar cerrarla
    portes.fermer()
    assert not portes.getOuvert()


