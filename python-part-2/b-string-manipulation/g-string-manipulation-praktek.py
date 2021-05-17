judulArtikel = [
    "Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
    "Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
    "Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
    "Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
    "Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
    "Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
    "Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
    "Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
    "Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
    "Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]

jumlahArtikelJeruk = 0
jumlahArtikelSalak = 0
for judul in judulArtikel:
    if judul.count("Jeruk") > 0:
        jumlahArtikelJeruk += 1
    if judul.count("Salak") > 0:
        jumlahArtikelSalak += 1
print(jumlahArtikelJeruk)
print(jumlahArtikelSalak)

print("---------------")

judulArtikel = [
    "Buah Salak Baik untuk Mata", "Buah Salak Kaya Potasium", 
    "Buah Jeruk Kaya Vitamin C", "Buah Salak Kaya Manfaat", 
    "Salak Baik untuk Jantung", "Jeruk dapat Memperkuat Tulang", 
    "Jeruk Mencegah Penyakit Asma", "Jeruk Memperkuat Gigi", 
    "Jeruk Mencegah Kolesterol Jahat", "Salak Mencegah Diabetes", 
    "Salak Memperkuat Dinding Usus", "Salak Baik untuk Darah",
    "Jeruk Kaya Manfaat untuk Jantung", "Salak si Kecil yang Baik", 
    "Jeruk dan Salak Buah Kaya Manfaat", "Buah Jeruk Enak",
    "Tips Panen Jeruk Ribuan Kilo", "Tips Bertanam Salak", 
    "Salak Manis untuk Berbuka", "Jeruk Baik untuk Wajah"
]
kataPositif = ["Kaya", "Baik", "Mencegah", "Memperkuat"]
kataPositifJeruk = 0
kataPositifSalak = 0
for judul in judulArtikel: 
    for kata in kataPositif:
        if judul.count("Jeruk") > 0 and judul.count(kata) > 0: 
            kataPositifJeruk += 1
        if judul.count("Salak") > 0 and judul.count(kata) > 0:
            kataPositifSalak += 1
print(kataPositifJeruk) 
print(kataPositifJeruk)