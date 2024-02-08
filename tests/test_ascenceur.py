import unittest
from ascenceur import Ascenceur

class TestAscenseur(unittest.TestCase):
    def test_initial_state(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        self.assertEqual(ascenseur.etage_actuel, 0)
        self.assertEqual(ascenseur.etage_max, 10)
        self.assertEqual(ascenseur.etage_min, 0)
        self.assertIsNone(ascenseur.direction)
        self.assertFalse(ascenseur.arret)
        self.assertEqual(ascenseur.destinations, [])

    def test_ajouter_destination_if(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.ajouter_destination(5)
        self.assertEqual(ascenseur.destinations, [5])
        ascenseur.ajouter_destination(3)
        self.assertEqual(ascenseur.destinations, [3, 5])
        ascenseur.ajouter_destination(7)
        self.assertEqual(ascenseur.destinations, [3, 5, 7])
    
    def test_ajouter_destination_else(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3, 5, 7]
        ascenseur.ajouter_destination(3)
        self.assertEqual(ascenseur.destinations, [3, 5, 7])
        ascenseur.ajouter_destination(5)
        self.assertEqual(ascenseur.destinations, [3, 5, 7])
        ascenseur.ajouter_destination(7)
        self.assertEqual(ascenseur.destinations, [3, 5, 7])

    def test_monter_if(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.monter()
        self.assertEqual(ascenseur.etage_actuel, 1)
        ascenseur.monter()
        self.assertEqual(ascenseur.etage_actuel, 2)
    
    def test_monter_else(self):
        ascenceur = Ascenceur(etage_max=10, etage_min=0)
        ascenceur.etage_actuel = 10
        ascenceur.monter()
        self.assertEqual(ascenceur.etage_actuel, 10)
        ascenceur.etage_actuel = 11
        ascenceur.monter()
        self.assertEqual(ascenceur.etage_actuel, 11)

    def test_descendre_if(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.descendre()
        self.assertEqual(ascenseur.etage_actuel, 4)
        ascenseur.descendre()
        self.assertEqual(ascenseur.etage_actuel, 3)

    def test_descendre_else(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.descendre()
        self.assertEqual(ascenseur.etage_actuel, 0)
        ascenseur.etage_actuel = -1
        ascenseur.descendre()
        self.assertEqual(ascenseur.etage_actuel, -1)

    def test_choisir_direction_destinations_bas(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3]
        ascenseur.etage_actuel = 5
        ascenseur.choisir_direction()
        self.assertEqual(ascenseur.direction, "bas")

    def test_choisir_direction_destinations_haut(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3]
        ascenseur.etage_actuel = 1
        ascenseur.choisir_direction()
        self.assertEqual(ascenseur.direction, "haut")
    
    def test_choisir_direction_destinations_none(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3]
        ascenseur.etage_actuel = 3
        ascenseur.choisir_direction()
        self.assertIsNone(ascenseur.direction)
    
    def test_choisir_direction_destinations_vide(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.choisir_direction()
        self.assertIsNone(ascenseur.direction)

    def test_bouger_bas(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3]
        ascenseur.etage_actuel = 5
        ascenseur.bouger()
        self.assertEqual(ascenseur.direction, "bas")
        self.assertEqual(ascenseur.etage_actuel, 4)
        ascenseur.bouger()
        self.assertEqual(ascenseur.etage_actuel, 3)

    def test_bouger_haut(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3]
        ascenseur.etage_actuel = 1
        ascenseur.bouger()
        self.assertEqual(ascenseur.direction, "haut")
        self.assertEqual(ascenseur.etage_actuel, 2)
        ascenseur.bouger()
        self.assertEqual(ascenseur.etage_actuel, 3)
        
    def test_bouger_none(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.bouger()
        self.assertIsNone(ascenseur.direction)
        self.assertEqual(ascenseur.etage_actuel, 0)
        ascenseur.destinations = [3]
        ascenseur.etage_actuel = 3
        ascenseur.bouger()
        self.assertIsNone(ascenseur.direction)
        self.assertEqual(ascenseur.etage_actuel, 3)

    def test_ouvrir_porte(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.ouvrir_porte()
        self.assertTrue(ascenseur.arret)

    def test_fermer_porte_destinations_in(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [5, 6, 7]
        ascenseur.etage_actuel = 5
        ascenseur.ouvrir_porte()  
        self.assertTrue(ascenseur.arret) 
        ascenseur.fermer_porte()  
        self.assertFalse(ascenseur.arret) 
        self.assertEqual(ascenseur.destinations, [6, 7])

    def test_fermer_porte_destinations_out(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [6, 7]
        ascenseur.etage_actuel = 5
        ascenseur.ouvrir_porte()  
        self.assertTrue(ascenseur.arret) 
        ascenseur.fermer_porte()  
        self.assertFalse(ascenseur.arret) 
        self.assertEqual(ascenseur.destinations, [6, 7])
    
    def test_fermer_porte_destinations_vide(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = []
        ascenseur.etage_actuel = 5
        ascenseur.ouvrir_porte()  
        self.assertTrue(ascenseur.arret) 
        ascenseur.fermer_porte()  
        self.assertFalse(ascenseur.arret) 
        self.assertEqual(ascenseur.destinations, [])

    def test_redemarer_arret(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.destinations = [6]
        ascenseur.ouvrir_porte()
        ascenseur.redemarrer()
        self.assertEqual(ascenseur.etage_actuel, 5)
        self.assertTrue(ascenseur.arret)

    def test_redemarer_destinations_in(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.destinations = [5]
        ascenseur.redemarrer()
        self.assertEqual(ascenseur.etage_actuel, 5)
        self.assertFalse(ascenseur.arret)
    
    def test_redemarer_arret_destinations_in(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.destinations = [5]
        ascenseur.ouvrir_porte()
        ascenseur.redemarrer()
        self.assertEqual(ascenseur.etage_actuel, 5)
        self.assertTrue(ascenseur.arret)

    def test_redemarer_destinations_out(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.destinations = [6]
        ascenseur.redemarrer()
        self.assertEqual(ascenseur.etage_actuel, 6)
        self.assertFalse(ascenseur.arret)
