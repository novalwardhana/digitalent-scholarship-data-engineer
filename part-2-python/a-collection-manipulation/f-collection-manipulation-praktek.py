# Data keuangan
keuangan = {
    'pengeluaran': [2, 2.5, 2.25, 2.5, 3.2, 2.5, 3.5, 4, 3],
    'pemasukan': [7.8, 7.5, 9, 7.6, 7.2, 7.5, 7, 10, 7.5]
}

totalPengeluaran = 0
totalPemasukan = 0

for biaya in keuangan['pengeluaran']:
    totalPengeluaran += biaya

for biaya in keuangan['pemasukan']:
    totalPemasukan += biaya

rataRataPengeluaran = totalPengeluaran / len(keuangan['pengeluaran'])
rataRataPemasukan = totalPemasukan / len(keuangan['pemasukan'])

print("Rata-rata Pengeluaran: ", rataRataPengeluaran)
print("Rata-rata pemasukan: ", rataRataPemasukan)