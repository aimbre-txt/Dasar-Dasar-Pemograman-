import math
def kubus(sisi) :
    hasil = math.pow(sisi, 3)
    return hasil

def balok(panjang, lebar, tinggi) :
    hasil = panjang * lebar * tinggi
    return hasil
print(kubus(3)) 

def prisma(alas, tinggi) :
    luas_alas = 0.5 * alas * tinggi
    hasil = luas_alas * tinggi
    return hasil

print(prisma(4, 6))

def tabung(jari_jari, tinggi) :
    hasil = math.pi * math.pow(jari_jari, 2) * tinggi
    return hasil

print(tabung(7, 10))

def kerucut(jari_jari, tinggi) :
    hasil = (1/3) * math.pi * math.pow(jari_jari, 2) * tinggi
    return hasil

print(kerucut(5, 12))