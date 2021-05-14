# Fungsi dengan argumen default
def fungsiDenganArgumenDefault(namaDepan, namaBelakang, usia = 25, alamat = "Yogyakarta"):
    print("Nama: ", namaDepan + " " + namaBelakang)
    print("Usia: ", usia)
    print("Alamat: ", alamat, "\n---------------\n")

fungsiDenganArgumenDefault("Noval", "Wardhana")
fungsiDenganArgumenDefault("Kusuma", "W", 26, "Manchester")