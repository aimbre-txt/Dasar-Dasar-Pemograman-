import math

def persegi(sisi):
    hasil = sisi * sisi
    return hasil    

def persegiPanjang(panjang, lebar):
    hasil = panjang * lebar
    return hasil

def segitiga(alas, tinggi):
    hasil = 0.5 * alas * tinggi
    return hasil

def lingkaran(jari_jari):
    hasil = math.pi * math.pow(jari_jari, 2)
    return hasil

def jajarGanjar(alas, tinggi):
    hasil = alas * tinggi
    return hasil