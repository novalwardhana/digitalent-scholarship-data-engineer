class karyawan:
    namaPerusahaan = "ABCD"
    def __init__(self, nama, usia, pendapatan, alamat):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.alamat = alamat
        if usia > 20:
            self.pendapatan += 1500000
        self.rawData = {
            "nama": self.nama,
            "usia": self.usia,
            "pendapatan": self.pendapatan,
            "alamat": self.alamat
        }

karyawan1 = karyawan('Noval', 18, 1500000, "Bantul")
karyawan2 = karyawan('Kusuma', 21, 3000000, "Gunungkidul")
karyawan3 = karyawan("wardhana", 25, 4500000, "Kulon Progo")
karyawan1.__class__.namaPerusahaan = "Microsoft"

print("Karyawan 1")
print("nama: ", karyawan1.nama)
print("usia: ", karyawan1.usia)
print("pendapatan: ", karyawan1.pendapatan)
print("alamat: ", karyawan1.alamat)
print("nama perusahaan: ", karyawan1.namaPerusahaan)
print("raw data: ", karyawan1.rawData, "\n------------------\n")

print("Karyawan 2")
print("nama: ", karyawan2.nama)
print("usia: ", karyawan2.usia)
print("pendapatan: ", karyawan2.pendapatan)
print("alamat: ", karyawan2.alamat)
print("nama perusahaan: ", karyawan2.namaPerusahaan)
print("raw data: ", karyawan2.rawData, "\n---------------\n")

print("Karyawan 3")
print("nama: ", karyawan3.nama)
print("usia: ", karyawan3.usia)
print("pendapatan: ", karyawan3.pendapatan)
print("alamat: ", karyawan3.alamat)
print("nama perusahaan: ", karyawan3.namaPerusahaan)
print("raw data: ", karyawan3.rawData, "\n---------------\n")

print("Total pendapatan: ", karyawan1.pendapatan + karyawan2.pendapatan + karyawan3.pendapatan)
