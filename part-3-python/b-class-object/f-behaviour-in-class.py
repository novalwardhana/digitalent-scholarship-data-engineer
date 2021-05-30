class Karyawan:
    namaPerusahaan = "ABCD"
    insentifLembur = 350000
    def __init__(self, nama, usia, pendapatan, alamat):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.alamat = alamat
        self.pendapatanTambahan = 0
        if usia > 20:
            self.pendapatan += 1500000
        self.rawData = {
            "nama": self.nama,
            "usia": self.usia,
            "pendapatan": self.pendapatan,
            "alamat": self.alamat,
            "pendapatanTambahan": self.pendapatanTambahan
        }
    def lembur(self):
        self.pendapatanTambahan += self.insentifLembur
    def tambahanProyek(self, insentif):
        self.pendapatanTambahan += insentif
    def totalPendapatan(self):
        return self.pendapatan + self.pendapatanTambahan

karyawan1 = Karyawan("Aksara", 18, 3000000, "Bandung")
karyawan1.lembur()
karyawan1.lembur()
karyawan1.tambahanProyek(500000)
karyawan1.lembur()
karyawan1.tambahanProyek(50000)
print("Karyawan 1: ", karyawan1.nama)
print("Total pendapatan: ", karyawan1.totalPendapatan(), "\n---------------\n")

karyawan2 = Karyawan("Senja", 21, 4500000, "Jakarta")
karyawan2.lembur()
karyawan2.tambahanProyek(50000)
karyawan2.tambahanProyek(100000)
print("Karyawan 2: ", karyawan2.nama)
print("Total pendapatan: ", karyawan2.totalPendapatan(), "\n---------------\n")

print("Total keseluruhan: ", karyawan1.totalPendapatan() + karyawan2.totalPendapatan())