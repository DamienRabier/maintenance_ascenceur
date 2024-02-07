import unittest


class Ascenceur:
    def __init__(self, etage_max, etage_min):
        self.etage_actuel = 0
        self.etage_max = etage_max
        self.etage_min = etage_min
        self.direction = None  # Puede ser 'haut', 'bas' o None
        self.destinations = []
        self.arret = False

    def ajouter_destination(self, etage):
        if etage not in self.destinations:
            self.destinations.append(etage)
            self.destinations.sort()

    def monter(self):
        if self.etage_actuel < self.etage_max:
            self.etage_actuel += 1
            self.direction = "haut"

    def descendre(self):
        if self.etage_actuel > self.etage_min:
            self.etage_actuel -= 1
            self.direction = "bas"

    def choisir_direction(self):
        if self.destinations:
            if self.etage_actuel < self.destinations[0]:
                self.direction = "haut"
            elif self.etage_actuel > self.destinations[0]:
                self.direction = "bas"
            else:
                self.direction = None

    def bouger(self):
        self.choisir_direction()
        if self.direction == "haut":
            self.monter()
        elif self.direction == "bas":
            self.descendre()

    def ouvrir_porte(self):
        print(f"Porte ouverte à l'étage {self.etage_actuel}.")
        self.arret = True

    def fermer_porte(self):
        print(f"Porte fermée à l'étage {self.etage_actuel}.")
        self.arret = False
        if self.etage_actuel in self.destinations:
            self.destinations.remove(self.etage_actuel)

class TestAscenseur(unittest.TestCase):
    def test_initial_state(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        self.assertEqual(ascenseur.etage_actuel, 0)
        self.assertEqual(ascenseur.etage_max, 10)
        self.assertEqual(ascenseur.etage_min, 0)
        self.assertIsNone(ascenseur.direction)
        self.assertFalse(ascenseur.arret)
        self.assertEqual(ascenseur.destinations, [])

    def test_ajouter_destination(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.ajouter_destination(5)
        self.assertEqual(ascenseur.destinations, [5])
        ascenseur.ajouter_destination(3)
        self.assertEqual(ascenseur.destinations, [3, 5])
        ascenseur.ajouter_destination(7)
        self.assertEqual(ascenseur.destinations, [3, 5, 7])

    def test_monter(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.monter()
        self.assertEqual(ascenseur.etage_actuel, 1)
        ascenseur.monter()
        self.assertEqual(ascenseur.etage_actuel, 2)

    def test_descendre(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.descendre()
        self.assertEqual(ascenseur.etage_actuel, 4)
        ascenseur.descendre()
        self.assertEqual(ascenseur.etage_actuel, 3)

    def test_choisir_direction(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3, 7, 9]
        ascenseur.etage_actuel = 5
        ascenseur.choisir_direction()
        self.assertEqual(ascenseur.direction, "bas")
        ascenseur.etage_actuel = 2
        ascenseur.choisir_direction()
        self.assertEqual(ascenseur.direction, "haut")
        ascenseur.etage_actuel = 7
        ascenseur.choisir_direction()
        self.assertIsNone(ascenseur.direction)

    def test_bouger(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.destinations = [3, 7, 9]
        ascenseur.etage_actuel = 5
        ascenseur.bouger()
        self.assertEqual(ascenseur.direction, "bas")
        self.assertEqual(ascenseur.etage_actuel, 4)
        ascenseur.bouger()
        self.assertEqual(ascenseur.etage_actuel, 3)
        ascenseur.bouger()  # Doit s'arrêter au 3ème étage et ouvre la porte
        self.assertTrue(ascenseur.arret)
        ascenseur.fermer_porte()
        self.assertFalse(ascenseur.arret)
        self.assertEqual(ascenseur.destinations, [7, 9])

    def test_ouvrir_porte(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.ouvrir_porte()
        self.assertTrue(ascenseur.arret)

    def test_fermer_porte(self):
        ascenseur = Ascenceur(etage_max=10, etage_min=0)
        ascenseur.etage_actuel = 5
        ascenseur.ouvrir_porte()  # Ouvrir la porte d'abord
        self.assertTrue(ascenseur.arret)  # Vérifier si la porte est ouverte
        ascenseur.fermer_porte()  # Fermer la porte
        self.assertFalse(ascenseur.arret)  # Vérifier si la porte est fermée
        self.assertEqual(ascenseur.destinations, [])  # S'assurer que les destinations sont vides si l'étage actuel est une destination

if __name__ == "__main__":
    unittest.main()
