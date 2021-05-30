class Karyawan:
    namaPerusahaan = "ABCD"
    __insentifLembur = 150000
    def __init__(self, nama, usia, pendapatan, alamat):
        self.__nama = nama
        self.__usia = usia
        self.__pendapatan = pendapatan
        self.__alamat = alamat
        self.__pendapatanTambahan = 0
    def getNama(self):
        return self.__nama
    def getUsia(self):
        return self.__usia
    def getAlamat(self):
        return self.__alamat
    def lembur(self):
        self.__pendapatanTambahan += self.__insentifLembur
    def tambahanProyek(self, insentifProyek):
        self.__pendapatanTambahan += insentifProyek
    def totalPendapatan(self):
        return self.__pendapatan + self.__pendapatanTambahan

karyawan1 = Karyawan("Aksara", 20, 2500000, "Solo")
karyawan1.lembur()
karyawan1.tambahanProyek(500000)
karyawan1.__class__.namaPerusahaan = "GoTo"
print("Karyawan 1")
print("Nama: ", karyawan1.getNama())
print("Usia: ", karyawan1.getUsia())
print("Alamat: ", karyawan1.getAlamat())
print("Perusahaan: ", karyawan1.namaPerusahaan)
print("Total pendapatan: ", karyawan1.totalPendapatan(), "\n---------------\n")

karyawan2 = Karyawan("Senja", 22, 3500000, "Sukoharjo")
karyawan2.lembur()
karyawan2.tambahanProyek(500000)
print("Karyawan 2")
print("Nama: ", karyawan2.getNama())
print("Usia: ", karyawan2.getUsia())
print("Alamat: ", karyawan2.getAlamat())
print("Perusahaan: ", karyawan2.namaPerusahaan)
print("Total pendapatan: ", karyawan2.totalPendapatan())