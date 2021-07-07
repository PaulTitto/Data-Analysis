from geometri.persegipanjang import PersegiPanjang
from geometri.segitiga import SegiTiga

p1 = PersegiPanjang(10, 3)
print(p1.info())
print(p1.hitung_luas)


s1 = SegiTiga(10, 3)
print(s1.info())
print(s1.hitung_luas)

print(''\nMencoba membuat object dari kelas BangunRuang)
b1 = BangunRuang()
b1.info()