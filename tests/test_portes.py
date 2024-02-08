from portes import Portes

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
    portes.ouvrir()  # Assurez-vous que la porte est ouverte avant de tenter de la fermer
    portes.fermer()
    assert not portes.getOuvert()

def test_get_etage():
    portes = Portes(etage=3)
    assert portes.getEtage() == 3

def test_set_etage():
    portes = Portes(etage=4)
    portes.setEtage(5)
    assert portes.getEtage() == 5
    
def test_get_ouvert():
    portes = Portes(etage=6)
    assert not portes.getOuvert()

def test_set_ouvert():
    portes = Portes(etage=7)
    portes.setOuvert(True)
    assert portes.getOuvert()
    
def test_str():
    portes = Portes(etage=8)
    assert str(portes) == "Etage: 8"