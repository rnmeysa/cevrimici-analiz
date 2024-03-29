# -*- coding: utf-8 -*-
"""analizhesabı.ipynb adlı not defterinin kopyası

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hqattIRmiN-Dn3l-9GyE4ySbY317FNzI
"""

def su_kalitesi_hesapla(Ph, KOI, BOI, fosfor, sülfat, sıcaklık, amonyum, nitrat, nitrit, klor, renk, bulanıklık, siyanür, çözünmüş_oksijen, ec):
    sonuclar = ""

    if 6.5 <= Ph <= 9.5:
        sonuclar += "PH: İyi\n"
    else:
        sonuclar += "PH: Kötü\n"

    if 1.6 < KOI < 2.5:
        sonuclar += "KOI: İyi\n"
    else:
        sonuclar += "KOI: Kötü\n"

    if 1.6 < BOI < 2.5:
        sonuclar += "BOI: İyi\n"
    else:
        sonuclar += "BOI: Kötü\n"

    if 0.4 < fosfor < 5.0:
        sonuclar += "Fosfor: İyi\n"
    else:
        sonuclar += "Fosfor: Kötü\n"

    if 7 < sülfat < 131:
        sonuclar += "Sülfat: İyi\n"
    else:
        sonuclar += "Sülfat: Kötü\n"

    if 0.5 < siyanür < 0.7:
        sonuclar += "siyanür: İyi\n"
    else:
        sonuclar += "siyanür: Kötü\n"

    if 0 < çözünmüş_oksijen < 14.6:
        sonuclar += "çözünmüş_oksijen: İyi\n"
    else:
        sonuclar += "çözünmüş_oksijen: Kötü\n"

    if 0 < ec < 0.25:
        sonuclar += "ec: İyi\n"
    else:
        sonuclar += "ec: Kötü\n"

    if 0 < nitrat <= 50:
        sonuclar += " Nitrat: İyi\n"
    else:
        sonuclar += "Nitrat: Kötü\n"

    if 10 < nitrit < 45:
        sonuclar += " nitrit: İyi\n"
    else:
        sonuclar += "nitrit: Kötü\n"

    if 0.6 < klor < 0.8:
        sonuclar += "klor: İyi\n"
    else:
        sonuclar += "klor: Kötü\n"

    if 15 < renk < 20:
        sonuclar += " renk: İyi\n"
    else:
        sonuclar += " renk: Kötü\n"

    if 4.0 < bulanıklık < 5.0:
        sonuclar += "bulanıklık: İyi\n"
    else:
        sonuclar += "bulanıklık: Kötü\n"

    if 0.5 < amonyum < 10:
        sonuclar += "amonyum: İyi\n"
    else:
        sonuclar += "amonyum: Kötü\n"

    return sonuclar

Ph = float(input("Su pH değerini girin: "))
KOI = float(input("KOI değerini girin: "))
BOI = float(input("BOI değerini girin: "))
fosfor = float(input("Fosfor değerini girin: "))
sülfat = float(input("Sülfat değerini girin: "))
sıcaklık = float(input("Sıcaklık değerini girin: "))
amonyum = float(input("Amonyum değerini girin: "))
nitrat = float(input("Nitrat değerini girin: "))
nitrit = float(input("Nitrit değerini girin: "))
klor = float(input("Klor değerini girin: "))
renk = float(input("Renk değerini girin: "))
bulanıklık = float(input("Bulanıklık değerini girin: "))
siyanür = float(input("Siyanür değerini girin: "))
çözünmüş_oksijen = float(input("Çözünmüş oksijen değerini girin: "))
ec = float(input("EC değerini girin: "))

print("\nSu Kalitesi Değerlendirmesi:")
print("-" * 30)
print(su_kalitesi_hesapla(Ph, KOI, BOI, fosfor, sülfat, sıcaklık, amonyum, nitrat, nitrit, klor, renk, bulanıklık, siyanür, çözünmüş_oksijen, ec))

import matplotlib.pyplot as plt

def birim_donusturme(deger, birim):
    if birim == "ppm":
        return deger * 0.001
    elif birim == "mg/l":
        return deger
    elif birim == "g/l":
        return deger * 1000
    else:
        return "Bilinmeyen birim."
a = float(input("a değerini girin: "))
b = float(input("b değerini girin: "))
birim = input("Değerin birimini girin (ppm, mg/l, g/l): ")
# Değerleri belirli bir birim türüne dönüştürürsek
a = birim_donusturme(a, birim)
b = birim_donusturme(b, birim)
# Çubuk grafik oluşturma
x = [a, b]
y = ["a", "b"]
plt.figure(figsize=(8, 5))
plt.bar(y, x, color='blue')
plt.xlabel('Parametreler')
plt.ylabel('Değerler (' + birim + ')')
plt.title('a ve b Değerleri')
plt.show()

