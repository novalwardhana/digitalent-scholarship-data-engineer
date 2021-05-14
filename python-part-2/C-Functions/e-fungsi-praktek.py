# Fungsi rata-rata dan standar deviasi dalam list
print(">>> Fungsi rata-rata dan standar deviasi dalam list")
data1 = [70, 70, 70, 100, 100, 100, 120, 120, 150, 150]
data2 = [50, 60, 60, 50, 70, 70, 100, 80, 100, 90]

def hitungRataRata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rataRata = jumlah / len(data)
    return rataRata

def hitungStandarDeviasi(data):
    rataRata = hitungRataRata(data)
    varians = 0
    for item in data:
        varians += (item - rataRata) ** 2
    varians /= len(data)
    standarDeviasi = varians ** (1/2)
    return standarDeviasi

print("Standar deviasi data-1: ", hitungStandarDeviasi(data1))
print("Standar deviasi data-2: ", hitungStandarDeviasi(data2), "\n---------------\n")


# Fungsi rata-rata dan standar deviasi dalam dictionary
print(">>> Fungsi rata-rata dan standar deviasi dalam dictionary")
tabelProperti = {
    'luasTanah': [70, 70, 70, 100, 100, 100, 120, 120, 150, 150],
    'luasBangunan': [50, 60, 60, 50, 70, 70, 100, 80, 100, 90],
    'jarak': [15, 30, 55, 30, 25, 50, 20, 50, 50, 15],
    'harga': [500, 400, 300, 700, 1000, 650, 2000, 1200, 1800, 3000]
}

def hitungRataRata(data):
    jumlah = 0
    for item in data:
        jumlah += item
    rataRata = jumlah / len(data)
    return rataRata

def hitungStandarDeviasi(data):
    rataRata = hitungRataRata(data)
    varians = 0
    for item in data:
        varians += (item - rataRata) ** 2
    varians /= len(data)
    standarDeviasi = varians ** (1/2)
    return standarDeviasi

def deskripsiProperti(tabel):
    for key in tabel.keys():
        print("Rata-rata ", key, ": ", hitungRataRata(tabel[key]))
        print("Standar deviasi ", key, ":", hitungStandarDeviasi(tabel[key]))
        print("")

deskripsiProperti(tabelProperti)
