from flask import Flask
from bank import BankAccount
import os

app = Flask(__name__)

akun = BankAccount(1000)

@app.route('/')
def home():
    return """
    <h1>Halo! Nasabah Prioritas! Versi Otomatis </h1>
    <p>Aplikasi ini berjalan di dalam Docker Container!</p>
    <p>Coba cek saldo di: <a href="/saldo">/saldo</a></p>
"""

@app.route('/saldo')
def cek_saldo():
    jumlah = akun.cek_saldo()
    return f"<h2>Saldo Anda saat ini: Rp {jumlah}</h2>"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)