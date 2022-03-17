from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        # fumgsi yang dipanggil pertama kali saat object diciptakan
        self.p = p
        self.l = l

    def info(self):
        return f'Ini adalah object dari Persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self, p, l):
        return self.p * self.l