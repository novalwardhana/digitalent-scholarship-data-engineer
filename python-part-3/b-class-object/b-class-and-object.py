class karyawan:
    namaPerusahaan = 'Microsoft'
    
noval = karyawan()
print(noval.__class__.namaPerusahaan)
kusuma = karyawan()
print(kusuma.__class__.namaPerusahaan)
wardhana = karyawan()
print(wardhana.__class__.namaPerusahaan)

kusuma.__class__.namaPerusahaan = 'Google Foundation'
print(noval.__class__.namaPerusahaan)
print(kusuma.__class__.namaPerusahaan)
print(wardhana.__class__.namaPerusahaan)

wardhana.__class__.namaPerusahaan = 'Tokopedia'
print(noval.__class__.namaPerusahaan)
print(kusuma.__class__.namaPerusahaan)
print(wardhana.__class__.namaPerusahaan)
