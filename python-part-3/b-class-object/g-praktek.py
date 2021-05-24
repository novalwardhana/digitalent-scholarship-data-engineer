class Karyawan:
    def __init__(self, nama, usia, pendapatan, insentifLembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        if usia > 20:
            self.pendapatan += 500000
        self.pendapatanTambahan = 0
        self.insentifLembur = insentifLembur
    def lembur(self):
        self.pendapatanTambahan += self.insentifLembur
    def tambahanProyek(self, insentif):
        self.pendapatanTambahan += insentif
    def totalPendapatan(self):
        return self.pendapatan + self.pendapatanTambahan

class Perusahaan:
    def __init__(self, nama, alamat, nomorTelepon):
        self.nama = nama
        self.alamat = alamat
        self.nomorTelepon = nomorTelepon
        self.listKaryawan = []
    def aktifkanKaryawan(self, karyawan):
        self.listKaryawan.append(karyawan)
    def nonaktifkanKaryawan(self, namaKaryawan):
        nonaktifData = None
        for karyawan in self.listKaryawan:
            if karyawan.nama == namaKaryawan:
                nonaktifData = karyawan
                break
        if nonaktifData is not None:
            self.listKaryawan.remove(nonaktifData)

perusahaan = Perusahaan("Facebook Foundation", "Jakarta", "085654094056")
karyawan1 = Karyawan("Noval", 20, 2000000, 200000)
karyawan1.lembur()
karyawan1.tambahanProyek(1500)
karyawan2 = Karyawan("Kusuma", 21, 3000000, 300000)
karyawan2.lembur()
karyawan2.tambahanProyek(3500)
karyawan3 = Karyawan("Wardhana", 22, 4000000, 400000)
karyawan3.lembur()
karyawan3.tambahanProyek(4500)
perusahaan.aktifkanKaryawan(karyawan1)
perusahaan.aktifkanKaryawan(karyawan2)
perusahaan.aktifkanKaryawan(karyawan3)

print("Perusahaan: ", perusahaan.nama)
print("Alamat: ", perusahaan.alamat)
print("Nomor telepon: ", perusahaan.nomorTelepon)
for index in range(len(perusahaan.listKaryawan)):
    print("- Karyawan", index+1)
    print("  nama: ", perusahaan.listKaryawan[index].nama)
    print("  usia: ", perusahaan.listKaryawan[index].usia)
    print("  alamat: ", perusahaan.listKaryawan[index].totalPendapatan())