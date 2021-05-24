class Karyawan:
    namaPerusahaan = "ABC"
    insentifLembur = 125000
    def __init__(self, nama, usia, pendapatan):
        self.__nama = nama
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.__pendapatanTambahan = 0
    def getNama(self):
        return self.__nama
    def lembur(self):
        insentif = self.insentifLembur
        if self.__usia > 30:
            insentif *=2
        self.__pendapatanTambahan += insentif
    def tambahanProyek(self, nominal):
        self.__pendapatanTambahan += nominal
    def totalPendapatan(self):
        return self.__pendapatan + self.__pendapatanTambahan

karyawan1 = Karyawan("Ben", 29, 5000000)
print("Karyawan 1: ", karyawan1.getNama())
karyawan1.lembur()
karyawan1.lembur()
karyawan1.tambahanProyek(1000000)
print("Total pendapatan: ", karyawan1.totalPendapatan(), "\n---------------\n")

karyawan2 = Karyawan("Jodie", 32, 5000000)
karyawan2.lembur()
karyawan2.lembur()
karyawan2.tambahanProyek(1000000)
print("Karyawan 2: ", karyawan2.getNama())
print("Total pendapatan: ", karyawan2.totalPendapatan())