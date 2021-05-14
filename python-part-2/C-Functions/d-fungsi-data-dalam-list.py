# Dua buah data yang tersimpan dalam tipe list
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]

def hitungRataRata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rataRata = jumlah / len(data)
    return rataRata

print("Rata-rata data-1: ", hitungRataRata(data1))
print("Rata-rata data-2: ", hitungRataRata(data2))