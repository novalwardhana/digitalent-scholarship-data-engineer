class Karyawan:
    namaPerusahaan = "ABCD"
    insentifLembur = 275000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatanTambahan = 0
    def lembur(self):
        self.pendapatanTambahan += self.insentifLembur
    def tambahanProyek(self, nominal):
        self.pendapatanTambahan += nominal
    def totalPendapatan(self):
        return self.pendapatan + self.pendapatanTambahan

class AnalisisData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

class IlmuwanData(Karyawan):
    def __init__(self, nama, usia, pendapatan):
        super().__init__(nama, usia, pendapatan)

aksara = AnalisisData("Aksara", 20, 2500000)
aksara.lembur()
aksara.tambahanProyek(125000)
print("Analisis Data")
print("Nama: ", aksara.nama)
print("Usia: ", aksara.usia)
print("Total pendapatan: ", aksara.totalPendapatan(), "\n---------------\n")

senja = IlmuwanData("Senja", 21, 3500000)
senja.lembur()
senja.tambahanProyek(350000)
print("Ilmuwan Data")
print("Nama: ", senja.nama)
print("Usia: ", senja.usia)
print("Total pendapatan: ", senja.totalPendapatan())