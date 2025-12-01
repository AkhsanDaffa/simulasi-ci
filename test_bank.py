import unittest
from bank import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_setor_uang(self):
        akun = BankAccount(100)
        hasil = akun.setor(50)
        self.assertEqual(hasil, 150)
    
    def test_tarik_uang(self):
        akun = BankAccount(100)
        hasil = akun.tarik(30)
        self.assertEqual(hasil, 70)

if __name__ == '__main__':
    unittest.main()