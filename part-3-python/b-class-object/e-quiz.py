class Karyawan:
    namaPerusahaan = "ABCD"
    tunjanganTransportasi = 450000
    def __init__(self, nama, usia, pendapatan, alamat):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.alamat = alamat
        if usia > 21:
            self.pendapatan += 1600000
        self.rawData = {
            "nama": self.nama,
            "usia": self.usia,
            "pendapatan": self.pendapatan,
            "alamat": self.alamat
        }

karyawan1 = Karyawan("Novalita", 20, 3000000, "Bantul")
karyawan1.__class__.namaPerusahaan = "Google Foundation"
karyawan2 = Karyawan("Kusuma", 22, 4500000, "Sleman")

totalPengeluaran = karyawan1.__class__.tunjanganTransportasi
totalPengeluaran += karyawan2.__class__.tunjanganTransportasi
totalPengeluaran += karyawan1.pendapatan
totalPengeluaran += karyawan2.pendapatan
print("Nama perusahaan: ", karyawan2.namaPerusahaan)
print("Tunjangan transportasi: ", totalPengeluaran)