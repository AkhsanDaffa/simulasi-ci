class BankAccount:
    def __init__(self, saldo_awal=0):
        self.saldo = saldo_awal
    
    def setor(self, jumlah):
        self.saldo += jumlah
        print("Programmer B: Terima kasih nasabah.")
        return self.saldo
    
    def tarik(self, jumlah):
        if jumlah > self.saldo:
            raise ValueError("Saldo tidak mencukupi")
        self.saldo -= jumlah
        return self.saldo
    
    def cek_saldo(self):
        return self.saldo