import unittest
from progetto_banca import ContoCorrente

class TestBanca(unittest.TestCase):
    
    def setUp(self):
        """Eseguito prima di ogni test"""
        self.conto = ContoCorrente("Test User", 100, fido=50)

    def test_deposito(self):
        self.conto.deposita(50)
        self.assertEqual(self.conto.saldo, 150)

    def test_prelievo_con_fido(self):
        # Saldo 100 + Fido 50 = Max prelevabile 150
        self.conto.preleva(120) 
        self.assertEqual(self.conto.saldo, -20) # Deve andare in negativo

    def test_prelievo_fallito(self):
        self.conto.preleva(200) # Oltre il fido
        self.assertEqual(self.conto.saldo, 100) # Saldo non deve cambiare

if __name__ == "__main__":
    unittest.main()
