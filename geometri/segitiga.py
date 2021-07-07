from geometri.bangun_ruang import BangunRuang


class SegiTiga(BangunRuang):
    def __init__(self, a, t):
        # fumgsi yang dipanggil pertama kali saat object diciptakan
        self.a = a
        self.t = t

    def info(self):
        return f'Ini adalah object dari Segitiga dengan panjang = {self.a} dan lebar = {self.t}'

    def hitung_luas(self, a, t):
        return self.a * self.t / 2
