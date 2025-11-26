import bangunRuang as br
import bangunDatar as bd

print("---- BANGUN RUANG ----")
print(f"Kubus dengan sisi 3 cm memiliki volume {br.kubus(3)} cm³")
print(f"Balok dengan panjang 4 cm, lebar 5 cm, dan tinggi 6 cm memiliki volume {br.balok(4, 5, 6)} cm³")
print(f"Prisma dengan alas 4 cm dan tinggi 6 cm memiliki volume {br.prisma(4, 6)} cm³")
print(f"Tabung dengan jari-jari 7 cm dan tinggi 10 cm memiliki volume {br.tabung(7, 10)} cm³")
print(f"Kerucut dengan jari-jari 5 cm dan tinggi 12 cm memiliki volume {br.kerucut(5, 12)} cm³")

print("---- BANGUN DATAR ----")
print(f"Luas Persegi adalah ")
print(f"Luas Persegi Panjang adalah ")
print(f"Luas Segitiga adalah ")
print(f"Luas Lingkaran adalah ")
print(f"Luas JajarGanjar adalah", bd.jajarGanjar(5, 10) ) 