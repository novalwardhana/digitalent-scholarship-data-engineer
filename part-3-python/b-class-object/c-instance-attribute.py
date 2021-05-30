class karyawan:
    namaPerusahaan = "ABCD"
    def __init__(self, nama, usia, pendapatan, alamat):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.alamat = alamat
        self.rawData = {
            "nama": self.nama,
            "usia": self.usia,
            "pendapatan": self.pendapatan,
            "alamat": self.alamat
        }

noval = karyawan("Noval", 20, 123, "Bantul")
noval.__class__.namaPerusahaan = "LinkAja"
print("nama: ", noval.nama)
print("usia: ", noval.usia)
print("pendapatan: ", noval.pendapatan)
print("alamat: ", noval.alamat)
print("raw data: ", noval.rawData)
print("perusahaan: ", noval.namaPerusahaan, "\n---------------\n")

kusuma = karyawan("Kusuma", 21, 456, "Gunungkidul")
print("nama: ", kusuma.nama)
print("usia: ", kusuma.usia)
print("pendapatan: ", kusuma.pendapatan)
print("alamat: ", kusuma.alamat)
print("raw data: ", kusuma.rawData)
print("perusahaan: ", kusuma.namaPerusahaan)
